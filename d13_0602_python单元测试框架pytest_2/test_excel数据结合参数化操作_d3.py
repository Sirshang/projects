import pytest
from d2_excel操作 import all_data,new_all_data,read_excel
from d4_日志封装操作 import logger

# 测试任务：登录功能
def login(username, password):
    if not username or not password:
        return "用户名或密码不能为空"
    elif username == "admin" and password == "12345":
        return "登录成功"
    else:
        return "登录失败"

# 方式一：从excel中读取到的数据格式为：列表嵌套元组
# [('用例编号', '用例标题', '用户名', '密码', '期望结果'), (1, '数据正确，登录成功', 'admin', 12345, '登录成功'), (2, '密码错误，登录失败', 'admin', 122222, '登录失败'), (3, '密码为空，提示正确', 'admin', None, '用户名或密码不能为空'), (4, '用户为空，提示正确', None, 12345, '用户名或密码不能为空')]

# # 第一步：从excel中读取数据
# case_data = all_data[1:]  # 去除数据中的标题这一行的内容
# # 第二步：用数据去驱动1个用例进行多次执行
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

# 方式二：从excel中读取到的数据格式为：列表嵌套字典
#[{'用例编号': 1, '用例标题': '数据正确，登录成功', '用户名': 'admin', '密码': 12345, '期望结果': '登录成功'}, {'用例编号': 2, '用例标题': '密码错误，登录失败', '用户名': 'admin', '密码': 122222, '期望结果': '登录失败'}, {'用例编号': 3, '用例标题': '密码为空，提示正确', '用户名': 'admin', '密码': None, '期望结果': '用户名或密码不能为空'}, {'用例编号': 4, '用例标题': '用户为空，提示正确', '用户名': None, '密码': 12345, '期望结果': '用户名或密码不能为空'}]
#  # 第一步：从excel中读取数据
# case_data = new_all_data
# # 第二步：用数据去驱动1个用例进行多次执行
# @pytest.mark.parametrize('item',case_data)
# def testlogin_1(item):
#     print(item)
#     # # 测试数据取值----字典的取值
#     username = item['用户名']
#     passwd = item['密码']
#     excepted = item['期望结果']
#     # 实际结果
#     actual = login(username,passwd)
#     # 断言
#     assert actual == excepted


# 方式三：导入的是封装好的excel读取函数   ---推荐（更灵活，适配更多的场景）
 # 第一步：从excel中读取数据
file = '测试数据.xlsx'
case_data = read_excel(file,'登录')
logger.info(f'读取{file}文件登录sheet中的所有数据....')
# 第二步：用数据去驱动1个用例进行多次执行
@pytest.mark.parametrize('item',case_data)
def testlogin_1(item):
    print(item)
    logger.info(f'开始执行第{item["用例编号"]}条用例...')
    # # 测试数据取值----字典的取值
    username = item['用户名']
    passwd = item['密码']
    excepted = item['期望结果']
    logger.info(f'获取数据,用户名：{username},密码：{passwd},期望结果：{excepted}')
    # 实际结果
    actual = login(username,passwd)
    logger.info(f'执行操作，获取实际结果：{actual}')
    # 断言
    try:
        assert actual == excepted
        logger.info(f'第{item["用例编号"]}条用例断言成功')
    except:
        logger.error(f'第{item["用例编号"]}条用例断言失败')
        raise AssertionError

