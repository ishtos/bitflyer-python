import requests
import simplejson as json
import utils
from base import Base

class PublicApi(Base):
    def __init__(self):
        pass

    def getmarkets(self):
        return self.get(path="/v1/getmarkets")

    def markets(self):
        return self.get(path="/v1/markets")

    def getboard(self, params={"product_code": "BTC_JPY"}):
        return self.get(path="/v1/getboard", params=params)

    def board(self, params={"product_code": "BTC_JPY"}):
        return self.get(path="/v1/board", params=params)

    def getticker(self, params={"product_code": "BTC_JPY"}):
        return self.get(path="/v1/getticker", params=params)

    def ticker(self, params={"product_code": "BTC_JPY"}):
        return self.get(path="/v1/ticker", params=params)

    def getexecutions(self, params={"product_code": "BTC_JPY"}):
        return self.get(path="/v1/getexecutions", params=params)

    def executions(self, params={"product_code": "BTC_JPY"}):
        return self.get(path="/v1/executions", params=params)

    def getboardstate(self):
        return self.get(path="/v1/getboardstate")

    def gethealth(self):
        return self.get(path="/v1/gethealth")

    def getchats(self):
        return self.get(path="/v1/getchats")

    def get(self, path, params=None):
        r = requests.get(self.url + path, params=params)

        return utils.parse_response(r)