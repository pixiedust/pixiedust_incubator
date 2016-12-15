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
from IPython.core.magic import (Magics, magics_class, cell_magic)
import warnings
import ibm_graph
from ibm_graph import IBMGraphClient
from pixiedust.utils.shellAccess import ShellAccess
import re
import pandas as pd
from pixiedust.display import *

@magics_class
class PixiedustGremlinMagics(Magics):
    def __init__(self, shell):
        super(PixiedustGremlinMagics,self).__init__(shell=shell) 
        self.graph_client = None       

    def getGraphClient(self):
        if self.graph_client is None:
            api_url=ShellAccess.graphUrl
            username=ShellAccess.graphUsername
            password=ShellAccess.graphPassword
            self.graph_client = ibm_graph.IBMGraphClient(api_url, username, password)
        return self.graph_client

    def getLineOption(self, line, optionName):
        m=re.search(r"\b" + optionName + r"=(\S+)",line)
        return m.group(1) if m is not None else None

    def hasLineOption(self, line, optionName):
        return re.match(r"\b" + optionName + r"\b", line) is not None

    @cell_magic
    def gremlin(self, line, cell):
        results = self.getGraphClient().run_gremlin_query(cell)
        varName = self.getLineOption(line, "var")
        if varName is not None:
            ShellAccess[varName]=results
        pdFrame = self.toPandas(results)
        ShellAccess["pdFrame"]=pdFrame
        display(pdFrame)

    def toPandas(self, result):
        data = []
        for i, val in enumerate(result):
            data.append([])
            #data[i].append(val.id)
            for key in val.properties:
                data[i].append(val.properties[key])
            data[i].append(val.label)

        pdFrame = pd.DataFrame(data)
        pdFrame.columns = ['gender', 'age', 'name','type']
        return pdFrame

try:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        get_ipython().register_magics(PixiedustGremlinMagics)
except NameError:
    #IPython not available we must be in a spark executor\
    pass