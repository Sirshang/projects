import pytest
# 测试任务：登录功能
def login(username, password):
    if not username or not password:
        return "用户名或密码不能为空"
    elif username == "admin" and password == "12345":
        return "登录成功"
    else:
        return "登录失败"


# 第一步：准备数据
# 列表嵌套元组/列表嵌套列表----存在的问题：1）可读性差一些；2）如果用例中有增加列，会导致整个代码出现问题
# case_data = [(1,'数据正常，登录成功','admin','12345','登录成功'),
#              (2,'admin','122222','登录失败'),
#              (3,'','12345','用户名或密码不能为空'),
#              (4,'admin','','用户名或密码不能为空')]

# 第二步：用数据去驱动1个用例进行多次执行
# @pytest.mark.parametrize('item',case_data)
# def testlogin_1(item):
#     print(item)
#     # 测试数据取值----元组的取值
#     username = item[1]
#     passwd = item[2]
#     excepted = item[3]
#     # 实际结果
#     actual = login(username,passwd)
#     # 断言
#     assert actual == excepted


# 列表嵌套字典---推荐（可读性高，不会受数据增加或者减少影响）
case_data = [{'caseid':1,'标题':'数据正确，登录成功','用户名':'admin','密码':'12345','期望结果':'登录成功'},
             {'caseid':2,'用户名':'admin','密码':'122222','期望结果':'登录失败'},
             {'caseid':3,'用户名':'','密码':'12345','期望结果':'用户名或密码不能为空'},
             {'caseid':4,'用户名':'admin','密码':'','期望结果':'用户名或密码不能为空'}]

# 第二步：用数据去驱动1个用例进行多次执行
@pytest.mark.parametrize('item',case_data)
def testlogin_1(item):
    print(item)
    # 测试数据取值----字典的取值：字典名[key],字典名.get(key)
    # username = item['用户名']
    username = item.get('用户名')
    passwd = item['密码']
    excepted = item['期望结果']
    # 实际结果
    actual = login(username,passwd)
    # 断言
    assert actual == excepted


