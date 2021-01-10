class Base:
    url = "https://api.bitflyer.com"
     
    @staticmethod
    def parse_response(r):
        if r.text:
            return {"status_code": r.status_code, "response": r.json()}
        else:
            return {"status_code": r.status_code}