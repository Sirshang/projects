import pytest
from common.excel_read import read_excel  # 建议从项目目录下一层开始到
from common.get_logger import logger
import pathlib

# 测试任务：登录功能
def login(username, password):
    if not username or not password:
        return "用户名或密码不能为空"
    elif username == "admin" and password == "12345":
        return "登录成功"
    else:
        return "登录失败"

# 路径处理
# 1、绝对路径
# abs_file = r'D:\Pycharm_workspace\py61\d14_0605_python数据处理和路径处理\data\测试数据.xlsx'
# 2、相对路径
# relative_file = r'..\data\测试数据.xlsx'
# 3、pathlib来动态获取路径值---最稳定
# 第一步：先找到当前文件所在的目录
current_path = pathlib.Path(__file__).absolute()
print(current_path)
# 第二步：再去找项目目录
root_path = current_path.parent.parent
print(root_path)
# 第三步：再去拼接你需要的这个文件的目录
casedata_path = root_path / 'data/测试数据.xlsx'

case_data = read_excel(casedata_path,'登录')
# print(case_data)
logger.info(f'读取{casedata_path}文件登录sheet中的所有数据....')


# @pytest.mark.parametrize('item',case_data)
# def testlogin_1(item):
#     print(item)
#     logger.info(f'开始执行第{item["用例编号"]}条用例...')
#     # # 测试数据取值----字典的取值
#     username = item['用户名']
#     passwd = item['密码']
#     excepted = item['期望结果']
#     logger.info(f'获取数据,用户名：{username},密码：{passwd},期望结果：{excepted}')
#     # 实际结果
#     actual = login(username,passwd)
#     logger.info(f'执行操作，获取实际结果：{actual}')
#     # 断言
#     try:
#         assert actual == excepted
#         logger.info(f'第{item["用例编号"]}条用例断言成功')
#     except:
#         logger.error(f'第{item["用例编号"]}条用例断言失败')
#         raise AssertionError
#
