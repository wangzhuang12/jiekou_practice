# from commonDate.commonDate import CommonDate
# from conftest import http
# import random
# import pytest
#
# class Test_LoadUserInfo():
#
#     @pytest.mark.debug
#     def test_loadUserInfo(self):
#         #注册
#         nickname = str(random.randint(10000000,100000000))
#         mobile = '135' + nickname
#         path = "/user/saveOrUpdateUser"
#         data = {'nickName':'gm',
#                  'userName':mobile,
#                  'telNo':'',
#                  'email':'',
#                  'address':'',
#                  'roleIds':'',
#                  'regionId':1,
#                  'regionLevel':1}
#         resp_saveOrUpdateUser = http.post(path, data)
#         print(resp_saveOrUpdateUser)
#         assert resp_saveOrUpdateUser['code'] == 200
#         assert resp_saveOrUpdateUser['msg'] == '操作成功'
#
#         #登录
#         path1 = "/sys/login"
#         data = {'userName':data['userName'] ,
#                 'password':CommonDate.password}
#         resp_login = http.post(path1, data)
#         print(resp_login)
#         assert resp_login['code'] == 200
#         assert resp_login['msg'] == '操作成功'
#         userId = resp_login['object']['userId']
#         print(userId)
#
#
#     #查看信息
#         path = "/user/loadUserList"
#         data = {'pageCurrent': 1,
#                 'pageSize': 10,
#                 'nickName': "",
#                 'userName': "",
#                 'regionId': 1}
#         resp_loadUserList = http.post(path, data)
#         print(resp_loadUserList)
#         id = resp_loadUserList['object']['list'][0]['id']
#         print(id)
#         assert resp_loadUserList['code'] == 200
#         assert resp_loadUserList['msg'] == '操作成功'
#         assert id==userId
#

