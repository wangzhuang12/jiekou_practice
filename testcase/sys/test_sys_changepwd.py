from commonDate.commonDate import CommonDate
from conftest import http
import pytest
import allure

@allure.feature('修改密码模块')
class Test_ChangePwd():
    # 成功修改密码
    @allure.story('修改密码成功')
    # @pytest.mark.usefixtures("recover_pwd")
    def test_changPwd_success(self):
        path = "/sys/changePwd"
        data = {'userId':116,
                'userName': CommonDate.mobile,
                'oldPwd': CommonDate.password,
                'password':CommonDate.newpwd}
        resp_changePwd = http.post(path, data)
        # print(resp_changePwd)
        assert resp_changePwd['code'] == 200
        assert resp_changePwd['msg'] == '操作成功'




    #成功改回原来密码
    @allure.story('改回原来密码')
    def test_changPwd_successReturn(self):
        path = "/sys/changePwd"
        data = {'userId':116,
                'userName': CommonDate.mobile,
                'oldPwd': '1234567',
                'password':CommonDate.password}
        resp_changePwd = http.post(path, data)
        # print(resp_changePwd)
        assert resp_changePwd['code'] == 200
        assert resp_changePwd['msg'] == '操作成功'

    #错误类型：旧密码错误
    @allure.story('旧密码错误')
    def test_changPwd_fail_type1(self):
        path = "/sys/changePwd"
        data = {'userId':116,
                'userName': CommonDate.mobile,
                'oldPwd': '111111',
                'password':'1234567'}
        resp_changePwd = http.post(path, data)
        # print(resp_changePwd)
        assert resp_changePwd['code'] == 411
        assert resp_changePwd['msg'] == '旧密码错误'


    #错误类型：旧密码为空
    @allure.story('修改密码成功')
    def test_changPwd_fail_type2(self):
        path = "/sys/changePwd"
        data = {'userId': 116,
                'userName': CommonDate.mobile,
                'oldPwd': '',
                'password': '1234567'}
        resp_changePwd = http.post(path, data)
        # print(resp_changePwd)
        assert resp_changePwd['code'] == 411
        assert resp_changePwd['msg'] == '旧密码错误'


    # 错误类型：用户名错误
    @allure.story('用户名错误')
    def test_changPwd_fail_type3(self):
        path = "/sys/changePwd"
        data = {'userId': 123,
                'userName': '13594147301',
                'oldPwd': '123456',
                'password': '1234567'}
        resp_changePwd = http.post(path, data)
        # print(resp_changePwd)
        assert resp_changePwd['code'] == 411
        assert resp_changePwd['msg'] == '旧密码错误'


    # 错误类型：参数缺少
    @allure.story('参数缺少')
    def test_changPwd_fail_type4(self):
        path = "/sys/changePwd"
        data = {'userId': 116,
                'userName': '18734445192',

                'password': '1234567'}
        resp_changePwd = http.post(path, data)
        # print(resp_changePwd)
        assert resp_changePwd['code'] == 500
        assert resp_changePwd['msg'] == '内部服务器异常，请联系研发人员'

     # 错误类型：用户名错误
    @allure.story('用户名错误')
    def test_changPwd_fail_type5(self):
        path = "/sys/changePwd"
        data = {'userId': 213,
                'userName': '13594544446',
                'oldPwd': '123456',
                'password': '1234567'}
        resp_changePwd = http.post(path, data)
        # print(resp_changePwd)
        assert resp_changePwd['code'] == 411
        assert resp_changePwd['msg'] == '旧密码错误'



# @pytest.fixture()
# def recover_pwd():
#     yield
#     path = "/sys/changePwd"
#     data = {'userId': 116,
#             'userName': CommonDate.mobile,
#             'oldPwd': CommonDate.newpwd,
#             'password': CommonDate.password}
#     resp_changePwd = http.post(path, data)
#     # print(resp_changePwd)
#     assert resp_changePwd['code'] == 200
#     assert resp_changePwd['msg'] == '操作成功'

