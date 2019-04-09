import pytest
import requests
import json
from util.httpUtil import HttpUtil
from commonDate.commonDate import CommonDate

http = HttpUtil()

@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path = "/sys/login"
    data ={'userName':CommonDate.mobile,
           'password':CommonDate.password}
    resp_login = http.post(path,data)
    CommonDate.token=resp_login['object']['token']
    print("登陆成功")

    yield
    pathout = "/sys/logout"
    data =None
    resp_out = http.post(pathout,data)
    print("退出登录")




