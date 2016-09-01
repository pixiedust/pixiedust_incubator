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
import requests

class PixieDustSimpleSearchDisplay(Display):
  def doRender(self, handlerId):
    self.addProfilingTime = False

    sssSource = "http://sss-got.mybluemix.net"
    sssQuery = "*:*"
    sssArgs = self.options.get("sssArgs")

    if sssArgs is not None and len(sssArgs) > 0:
      for arg in sssArgs:
        if arg.startswith("http"):
          sssSource = arg
        else:
          sssQuery = arg

    self._addHTMLTemplate("simplesearch.html", sssQuery=sssQuery, sssSource=sssSource)
    self._addScriptElement("https://ibm-cds-labs.github.io/simple-search-js/simplesearch.js", checkJSVar="SimpleSearch", callback=None)