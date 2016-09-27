# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2016
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------
from pixiedust.display.display import *
from pixiedust.utils.javaBridge import PixiedustOutput
from IPython.display import display as ipythonDisplay,HTML
import json
import random

BEGINSTREAM = "@BEGINSTREAM@"
ENDSTREAM = "@ENDSTREAM@"

channelData = {}
class StreamingChannel(PixiedustOutput):
  def printOutput(self, s):
    self.sendChannel("stdout", s)
  
  def sendChannel(self, channel, data):
      #try to decode as a JSON object
      try:
        data = json.loads(data)
      except:
        pass

      if channel in channelData:
        channelData[channel].append(data)
      else:
        channelData[channel]=[data]  

def getTwitterData():
  print(json.dumps(channelData))
  channelData.clear()

class PixieDustTwitterDemo(Display):
  def startStream(self):
    get_ipython().run_cell_magic(
      "scala",
      "channel={0} receiver={1}".format(StreamingChannel.__module__ + "." + StreamingChannel.__name__, "com.ibm.cds.spark.samples.PixiedustStreamingTwitter$"),
      """
        val demo = com.ibm.cds.spark.samples.PixiedustStreamingTwitter;
        demo.setConfig("tweets.key", "{0}")
        demo.startStreaming()
      """.format(self.options.get("filter", ""))
    )

  def stopStream(self):
    get_ipython().run_cell_magic(
      "scala",
      "channel={0} receiver={1}".format(StreamingChannel.__module__ + "." + StreamingChannel.__name__, "com.ibm.cds.spark.samples.PixiedustStreamingTwitter$"),
      """
        val demo = com.ibm.cds.spark.samples.PixiedustStreamingTwitter;
        demo.stopStreaming();
        val __tweets = demo.createTwitterDataFrames(sqlContext);
      """
    )
    #print(ENDSTREAM)

  def doRender(self, handlerId):
    self.addProfilingTime = False
    stream = self.options.get("stream")

    if stream is None:
      self._addScriptElement("https://d3js.org/d3.v3.js", checkJSVar="d3", 
        callback=[self.renderTemplate("demoPieChart.js"), self.renderTemplate("demoGroupedChart.js")]
      )
      self._addHTMLTemplate("demoScript.html")
      self._addHTMLTemplate("demo.html")

    elif stream is True or str(stream).lower() == 'true':
      self.startStream()

    elif stream is False or str(stream).lower() == 'false':
      self.stopStream()
  def genStartStreamingExecuteCode(self):
    return self.renderTemplate("startStreaming.execute", 
      channel=StreamingChannel.__module__ + "." + StreamingChannel.__name__,
      receiver="com.ibm.cds.spark.samples.PixiedustStreamingTwitter$",
      scalaCode="val demo = com.ibm.cds.spark.samples.PixiedustStreamingTwitter;demo.startStreaming();print(\\\"done\\\")")
