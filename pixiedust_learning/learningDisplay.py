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

class PixieDustLearningDisplay(Display):
    def doRender(self, handlerId):

        if self.options.get("topic"):
            self._addHTMLTemplate("DashDB Twitter Car 2015 Python Notebook.ipynb")
        else:
            #hard code course for now, should come from cloudant later on
            courses=yaml.safe_load(self.renderTemplate("courses.json"))

            steps=[
                {"title": "Select the topic", "template": "selectTopic.html"},
                {"title": "Select the Category for XXX", "template": "selectCategory.html"},
                {"title": "Your course is almost ready!", "template": "configureCourse.html"},
            ]
            self._addHTMLTemplate("startWizard.html", courses=courses, steps=steps);