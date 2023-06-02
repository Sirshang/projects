# 测试任务：登录功能
def login(username, password):
    if not username or not password:
        return "用户名或密码不能为空"
    elif username == "admin" and password == "12345":
        return "登录成功"
    else:
        return "登录失败"

# 没有框架，自动化的实现
# 第一步：编写自动化脚本，针对测试用例实现
def valid_login_1():
    # - case1: 测试数据：admin,123456，期望结果：登录成功
    # 测试数据
    username = 'admin'
    passwd = '123456'
    excepted = '登录成功'
    # 实际结果
    actual = login(username,passwd)
    # 断言
    assert actual == excepted

def valid_login_2():
    # - case2: 测试数据：admin,122222，期望结果：提示登录失败
    # 测试数据
    username = 'admin'
    passwd = '122222'
    excepted = '登录失败'
    # 实际结果
    actual = login(username,passwd)
    # 断言
    assert actual == excepted

def valid_login_3():
    # - case3: 测试数据：用户名为空,123456，期望结果：提示用户名或密码不能为空
    # 测试数据
    username = ''
    passwd = '123456'
    excepted = '用户名或密码不能为空'
    # 实际结果
    actual = login(username,passwd)
    # 断言
    assert actual == excepted

def valid_login_4():
    # - case4: 测试数据：admin,密码为空，期望结果：提示用户名或密码不能为空
    # 测试数据
    username = 'admin'
    passwd = ''
    excepted = '用户名或密码不能为空'
    # 实际结果
    actual = login(username,passwd)
    # 断言
    assert actual == excepted

# 第二步：执行脚本（调用函数），得到用例执行结果
valid_login_1()
valid_login_2()
valid_login_3()
valid_login_4()


