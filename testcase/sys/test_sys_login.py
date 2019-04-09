# from commonDate.commonDate import CommonDate
# from conftest import http
#
#
# class Test_Login():
#     def test_login_success(self):
#         path = "/sys/login"
#         data = {'userName': CommonDate.mobile,
#                 'password': CommonDate.password}
#         resp_login = http.post(path, data)
#
#         assert resp_login['code'] == 200
#         assert resp_login['msg'] == '操作成功'
#         assert resp_login['object']['userId'] == 116
#
#     #错误类型：密码错误
#     def test_login_fail_type1(self):
#         path = "/sys/login"
#         data = {'userName': CommonDate.mobile,
#                 'password': '1234567'}
#         resp_login = http.post(path, data)
#         assert resp_login['code'] == 410
#         assert resp_login['msg'] == '用户名或密码错误'
#
#     # 错误类型：用户不存在
#     def test_login_fail_type2(self):
#         path = "/sys/login"
#         data = {'userName': '18734455192',
#                 'password': '123456'}
#         resp_login = http.post(path, data)
#         assert resp_login['code'] == 301
#         assert resp_login['msg'] == '用户不存在'
#
#         # 错误类型：用户名为空
#     def test_login_fail_type3(self):
#         path = "/sys/login"
#         data = {'userName': '',
#                 'password': '123456'}
#         resp_login = http.post(path, data)
#          # print(resp_login)
#         assert resp_login['code'] == 301
#         assert resp_login['msg'] == '用户不存在'
#
#     # 错误类型：用户名长度超出限制
#     def test_login_fail_type4(self):
#         path = "/sys/login"
#         data = {'userName': '1873445519244554333',
#                 'password': '123456'}
#         resp_login = http.post(path, data)
#         # print(resp_login)
#         assert resp_login['code'] == 301
#         assert resp_login['msg'] == '用户不存在'
#
#
#     # 错误类型：缺少参数
#     def test_login_fail_type5(self):
#         path = "/sys/login"
#         data = {
#             'password': '123456'}
#         resp_login = http.post(path, data)
#         print(resp_login)
#         assert resp_login['code'] == 301
#         assert resp_login['msg'] == '用户不存在'
#














#---------------------------------------------------------------------
# @pytest.fixture()
# def first_fixture():
#     a=[2,3,4,5,67]
#     for i in a:
#         print(i)

# class Test_login():
#
#     @pytest.mark.debug
#     def test_first(self):
#         print("我的第一个用例")
#         # assert 1==2
#
# # @pytest.mark.usefixtures("first_fixture")
#     def test_second(self):
#         print("我的第er个用例")
#         # assert 1==1
#
#     @pytest.mark.debug
#     def test_three(self):
#         print("我的第san个用例")
#         # assert 'a' in 'cb'
#
#     def test_four(self):
#         print("我的第si个用例")
#         # assert not 1==2
#
#     @pytest.mark.info
#     def test_five(self):
#         print("我的第wu个用例")
#         a=[2,2,2,3,4,4,5,4]
#         # assert not 1 in a
#
#
#     def test_six(self):
#         print("我的第liu个用例")
#          # assert not 1 in [12]

