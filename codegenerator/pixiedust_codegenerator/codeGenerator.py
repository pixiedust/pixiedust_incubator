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

class PixieDustCodeGenDisplay(Display):
    def doRender(self, handlerId):
        self.addProfilingTime = False

        topic = self.options.get("topic")
        codesource = self.options.get("codesource")
        
        if topic is None:
            codegenTopics = []
            codegenSource = None
            codegenSnippetId = str()
            codegenArgs = self.options.get("codeGenArgs")

            if codegenArgs is not None and len(codegenArgs) > 0:
                for arg in codegenArgs:
                    if arg.startswith("http"):
                        codegenSource = arg
                    else:
                        codegenSnippetId = arg

            if codegenSource is None:
                codegenSource = "https://ibm-watson-data-lab.github.io/pixiedust_incubator/codegen/codegen-default.json"

            resp = requests.get(codegenSource)
            if resp.status_code == requests.codes.ok:
                codegenTopics = yaml.safe_load(resp.text)
            else:
                codegenTopics = yaml.safe_load(self.renderTemplate("codeGen.json"))

            steps = [
                {"title": "Select the topic", "template": "selectTopic.html"},
                {"title": "Select the Code Snippet to generate", "template": "selectSnippet.html"},
                {"title": "Set Code Snippet variables", "template": "setVariables.html"}
            ]

            self._addHTMLTemplate("startWizard.html", codegenTopics=codegenTopics, steps=steps, codegenSubtopicId=codegenSnippetId)
        elif codesource is None or codesource == "undefined":
            self._addHTMLTemplate("snippets/notAvailable.json")
        elif codesource.startswith("http"):
            resp = requests.get(codesource)
            if resp.status_code == requests.codes.ok:
                self._addHTML(resp.text)
            else:
                self._addHTMLTemplate("snippets/notAvailable.json")
        else:
            self._addHTMLTemplate(codesource)