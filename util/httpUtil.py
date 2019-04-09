import requests
from commonDate.commonDate import CommonDate
import json

class HttpUtil:

    def __init__(self):
        self.http=requests.session()
        self.headers = {'Content-Type':'application/json;charset=UTF-8'}

    def post(self,path,data):
        data_json = json.dumps(data)
        host=CommonDate.host
        proxies=CommonDate.proxies
        if CommonDate.token is not None:
            self.headers['token'] = CommonDate.token
        resp_login = self.http.post(url=host+path,
                                     proxies=proxies,
                                     data=data_json,
                                     headers=self.headers)
        assert resp_login.status_code == 200
        resp_json = json.loads(resp_login.text)
        return resp_json
