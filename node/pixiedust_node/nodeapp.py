# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2017
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed unde
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

from pixiedust.display.app import *

@PixieApp
class NodeApp:
    @route(clicked="true")
    def _clicked(self):
        self._addHTMLTemplateString("""
<input option_clicked="false" type="button" value="You Clicked, Now Go back">
""")
        
    @route()
    def main(self):
        self._addHTMLTemplateString(
"""
<input option_clicked="true" type="button" value="Click Me">
"""
        )