
from commonDate.commonDate import CommonDate
from conftest import http
import allure

@allure.feature('获取用户信息模块')
class Test_GetUserInfo():

    @allure.story('成功获取用户信息')
    def test_getUserInfo(self):
        path = "/sys/getUserInfo"
        data = {'token': CommonDate.token}
        resp_userinfo = http.post(path, data)
        assert resp_userinfo['msg'] == '操作成功'
        assert resp_userinfo['code'] == 200

def test_sdf():
    print("111")