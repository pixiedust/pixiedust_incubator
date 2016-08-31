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
import yaml
import time
import json
import random

BEGINSTREAM = "@BEGINSTREAM@"
ENDSTREAM = "@ENDSTREAM@"

class PixieDustTwitterDemo(Display):
  def startStream(self):
    # TODO: start streaming
    print(BEGINSTREAM)
    maxcount = random.randrange(5,25)
    while True:
      msg = { \
        'message': 'streaming :: random > ' + str(maxcount), \
        'data':[ \
        { 'key': '#mars', 'value': random.randrange(1,10), 'sadness': random.randrange(1,10), 'joy': random.randrange(1,10), 'fear': random.randrange(1,10) }, \
        { 'key': '#venus', 'value': random.randrange(1,10), 'sadness': random.randrange(1,10), 'joy': random.randrange(1,10), 'fear': random.randrange(1,10) }, \
        { 'key': '#earth', 'value': random.randrange(1,10), 'sadness': random.randrange(1,10), 'joy': random.randrange(1,10), 'fear': random.randrange(1,10) }], \
        'tweets': [{ 'pic': 'http://github.com/DTAIEB.png?size=50', 'name': 'user'+str(random.randrange(1,1000)), 'tweet': 'tweet tweet chirp chirp '+str(maxcount)}]} 
      print(json.dumps(msg))
      time.sleep(1)
      maxcount = maxcount - 1
      if maxcount < 0:
        break
    self.stopStream()

  def stopStream(self):
    # TODO: stop streaming
    print(ENDSTREAM)

  def doRender(self, handlerId):
    self.addProfilingTime = False
    stream = self.options.get("stream")

    if stream is None:
      self._addHTMLTemplate('demoScript.html',prefix=self.getPrefix())
      self._addHTMLTemplate('demoPieChart.html',prefix=self.getPrefix())
      self._addHTMLTemplate('demoGroupedChart.html',prefix=self.getPrefix())
      self._addHTMLTemplate("demo.html")

    elif stream is True or str(stream).lower() == 'true':
      self.startStream()

    elif stream is False or str(stream).lower() == 'false':
      self.stopStream()
