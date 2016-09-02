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
        demo.startStreaming()
      """
    )

    '''
    print(BEGINSTREAM)
    maxcount = random.randrange(5,25)
    while True:
      msg = { \
        'message': 'streaming :: random > ' + str(maxcount), \
        'topHashtags': [[["#PushAwardsKathNiels",21],["#9DaysLeftForPushAwards",16],["#DolceAmoreMostViewedSerye",8],["#PushAwardsLizQuens",8],["#PBBReuniYONG",3]]], \
        'toneScores': [[
        ["x","agreeableness_big5","analytical","anger","confident","conscientiousness_big5","disgust","extraversion_big5","fear","joy","neuroticism_big5","openness_big5","sadness","tentative"],
        ["#PushAwardsKathNiels",68.02250000000001,12.435,9.935,4.6475,24.427500000000002,11.83,68.86,15.39,31.2125,44.9775,13.8525,21.1025,0.0],["#9DaysLeftForPushAwards",38.625,0.0,3.875,9.875,14.875,5.0,43.625,6.125,31.875,29.0,16.125,14.125,0.0],
        ["#DolceAmoreMostViewedSerye",35.065,0.0,11.19,0.0,21.375,13.315,43.125,10.565,22.565,24.125,6.065,15.5,21.25],
        ["#PushAwardsLizQuens",35.065,0.0,11.19,0.0,21.375,13.315,43.125,10.565,22.565,24.125,6.065,15.5,21.25],
        ["#PBBReuniYONG",46.165,0.0,3.835,0.0,31.5,9.335,46.165,14.5,30.165,10.835,10.5,11.335,15.335]
        ]], \
        'data':[ \
        { 'key': '#mars', 'value': random.randrange(1,10), 'sadness': random.randrange(1,10), 'joy': random.randrange(1,10), 'fear': random.randrange(1,10) }, \
        { 'key': '#venus', 'value': random.randrange(1,10), 'sadness': random.randrange(1,10), 'joy': random.randrange(1,10), 'fear': random.randrange(1,10) }, \
        { 'key': '#earth', 'value': random.randrange(1,10), 'sadness': random.randrange(1,10), 'joy': random.randrange(1,10), 'fear': random.randrange(1,10) }], \
        'tweets': [{ 'pic': 'http://github.com/DTAIEB.png?size=50', 'name': 'user'+str(random.randrange(1,1000)), 'tweet': 'tweet tweet chirp chirp '+str(maxcount), \
        'sentiment': { 'happiness': random.randrange(0,100), 'fear': random.randrange(0,100), 'joy': random.randrange(0,100), 'sadiness': random.randrange(0,100) }}]} 
      print(json.dumps(msg))
      time.sleep(1)
      maxcount = maxcount - 1
      if maxcount < 0:
        break
    self.stopStream()
    '''

  def stopStream(self):
    get_ipython().run_cell_magic(
      "scala",
      "channel={0} receiver={1}".format(StreamingChannel.__module__ + "." + StreamingChannel.__name__, "com.ibm.cds.spark.samples.PixiedustStreamingTwitter$"),
      """
        val demo = com.ibm.cds.spark.samples.PixiedustStreamingTwitter;
        demo.stopStreaming()
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
