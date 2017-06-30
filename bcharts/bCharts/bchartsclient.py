import httplib
from urlparse import urlparse
import json
import pyspark
from pyspark.sql import *

class Client(object):
    def __init__(self, client_id, secret, domain = "https://api.beta.bcharts.xyz", sc = None):
        self.client_id = client_id
        self.secret    = secret
        self.api_key   = client_id + ":" + secret

        parsed_uri  = urlparse(domain)
        self.domain = parsed_uri.netloc
        self.https  = (parsed_uri.scheme == "https")

        self.sc = sc

    # def create(self, payload, type):
    #     data = {
    #         'payload': payload,
    #         'redirect_type': 'json'
    #     }
    #
    #     result = self.request("POST", "/integrations/requests/upload/csv", data)
    #     return result

    def create(self, payload, chartType = ""):
        data = {
            'payload': payload,
            'redirect_type': 'json',
            'chart_type': chartType
        }

        chart = self.request("POST", "/integrations/requests/upload/csv", data)

        return BChart(chart["chartId"])


    def charts(self):
        toReturn = []

        for chart in self.request("GET", "/charts")["charts"]:
            toReturn.append(BChart(chart, self))

        return toReturn

    def chart(self, chartId):
        chart = self.request("GET", "/charts/" + chartId)["chart"]
        return BChart(chart, self)

    def request(self, method, endpoint, body = {}):

        if self.https:
            conn = httplib.HTTPSConnection(self.domain)
        else:
            conn = httplib.HTTPConnection(self.domain)

        headers = { 'Authorization' : 'Token token="%s"' %  self.api_key }

        if (len(body) == 0):
            conn.request(method, endpoint, headers=headers)
        else:
            headers['content-type'] = 'application/json'
            conn.request(method, endpoint, json.dumps(body), headers=headers)

        r1 = conn.getresponse()
        data = json.load(r1)

        return data



class BChart(object):
    def __init__(self, chartId, client = None):
        if type(chartId) is dict:
            self.chartId = chartId["_id"]
        else:
            self.chartId = chartId

        self.client = client

    def get_data(self):
        return self.client.request("GET", "/charts/" + self.chartId + "/data")

    def get_df(self):
        sqlContext = SQLContext(self.client.sc)
        data = [pyspark.sql.Row(**row) for row in self.get_data()]

        return sqlContext.createDataFrame(data)

    def set_data(self, data):
        if (type(data) is pyspark.sql.dataframe.DataFrame):
            data = [row.asDict() for row in data.collect()]

        return self.client.request("PUT", "/charts/" + self.chartId + "/data", { 'data': data })


    def add_data(self, data):
        if (type(data) is dict):
            data = [data]
        elif (type(data) is pyspark.sql.dataframe.DataFrame):
            data = [row.asDict() for row in data.collect()]

        return self.client.request("POST", "/charts/" + self.chartId + "/data", { 'data': data })

    def render(self):
        if (self.is_zeppelin()):
            print(self.to_zeppelin())
        else:
            return JupyterChart(self.chartId)

    def render_designer(self):
        if (self.is_zeppelin()):
            print(self.to_zeppelin_designer())
        else:
            return JupyterChartDesigner(self.chartId)

    def to_zeppelin(self):
        return """%html
        <iframe src='https://e.beta.bcharts.xyz/e/{1}' height='{2}px' width='{3}px'>""".format(self.chartId, h, w)


    def to_zeppelin_designer(self):
        return """%html

        <iframe src='https://beta.bcharts.xyz/d/{1}' height='{2}px' width='{3}px'>""".format(self.chartId, h, w)




    def is_zeppelin(self):
        try:
            if (type(z) is PyZeppelinContex):
                return True
        except:
            return False
        else:
            return False

        return False



class JupyterChart(object):
    def __init__(self, chartId):
        self.chartId = chartId


    def _repr_html_(self, h=400, w=800, sharelink=False):
        chartLink = ""
        if sharelink:
            chartLink = "<div><a href='https://e.beta.bcharts.xyz/e/" + str(self.chartId) + "' target='_blank'>Link to chart</a></div>"
        return chartLink + "<iframe src='https://e.beta.bcharts.xyz/e/" + self.chartId + "' height='" + str(h) + "px' width='" + str(w) + "px'></iframe>";


class JupyterChartDesigner(object):
    def __init__(self, chartId):
        self.chartId = chartId


    def _repr_html_(self, h=400, w=800, sharelink=False):
        return "<iframe src='https://e.beta.bcharts.xyz/d/" + self.chartId + "' height='" + str(h) + "px' width='" + str(w) + "px'></iframe>";

