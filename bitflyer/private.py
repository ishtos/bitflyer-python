import requests
import utils
import hmac
import hashlib
from base import Base


class PrivateApi(Base):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def getpermissions(self):
        return self.get("/v1/me/getpermissions")

    def getbalance(self):
        return self.get("/v1/me/getbalance")

    def getcollateral(self):
        return self.get("/v1/me/getcollateral")

    def getcollateralaccounts(self):
        return self.get("/v1/me/getcollateralaccounts")

    def getaddresses(self):
        return self.get("/v1/me/getaddresses")

    def getcoinins(self, **kwargs):
        return self.get("/v1/me/getcoinins", **kwargs)

    def getcoinouts(self, **kwargs):
        return self.get("/v1/me/getcoinouts", **kwargs)

    def getbankaccounts(self):
        return self.get("/v1/me/getbankaccounts")

    def getdeposits(self, **kwargs):
        return self.get("/v1/me/getdeposits", **kwargs)

    def withdraw(self, **kwargs):
        return self.post("/v1/me/withdraw", **kwargs)

    def getwithdrawals(self):
        return self.get("/v1/me/getwithdrawals")

    def sendchildorder(self, **kwargs):
        return self.post("/v1/me/sendchildorder", **kwargs)

    def cancelchildorder(self, **kwargs):
        return self.post("/v1/me/cancelchildorder", **kwargs)

    def sendparentorder(self, **kwargs):
        return self.post("/v1/me/sendparentorder", **kwargs)

    def cancelparentorder(self, **kwargs):
        return self.post("/v1/me/cancelparentorder", **kwargs)

    def cancelallchildorders(self, **kwargs):
        return self.post("/v1/me/cancelallchildorders", **kwargs)

    def getchildorders(self, **kwargs):
        return self.get("/v1/me/getchildorders", **kwargs)

    def getparentorders(self, **kwargs):
        return self.get("/v1/me/getparentorders", **kwargs)

    def getparentorder(self, **kwargs):
        return self.get("/v1/me/getparentorder", **kwargs)

    def getexecutions(self, **kwargs):
        return self.get("/v1/me/getexecutions", **kwargs)

    def getbalancehistory(self, **kwargs):
        return self.get("/v1/me/getbalancehistory", **kwargs)

    def getpositions(self, **kwargs):
        return self.get("/v1/me/getpositions", **kwargs)

    def getcollateralhistory(self, **kwargs):
        return self.get("/v1/me/getcollateralhistory", **kwargs)

    def gettradingcommission(self, params={"product_code": "ETH_JPY"}):
        return self.get("/v1/me/gettradingcommission", params)

    def get(self, path, params=None):
        url = self.url + path
        if params:
            path += "?"
            for key in params.keys():
                path += f"{key}={params[key]}&"
            path = path.strip("&")
        header = self.get_header(path, "GET")

        r = requests.get(url, headers=header, params=params)
        return utils.parse_response(r)

    def post(self, private_api, **kwargs):
        url = self.url + path
        data = str(kwargs)
        header = self.get_header(path, "POST", data)

        r = requests.post(url, headers=header, data=data)
        return utils.parse_response(r)

    def get_header(self, relative_url, method, data=None):
        timestamp = self.get_nonce()
        text = timestamp + method + relative_url
        if data:
            text += str(data)
        sign = self.get_sign(text)

        return {
            "ACCESS-KEY": self.api_key,
            "ACCESS-TIMESTAMP": timestamp,
            "ACCESS-SIGN": sign,
            "Content-Type": "application/json",
        }

    @staticmethod
    def get_nonce():
        return str(int(time.time() * 1000000))

    def get_sign(self, text):
        return hmac.new(
            self.api_secret.encode("utf-8"), text.encode("utf-8"), hashlib.sha256
        ).hexdigest()