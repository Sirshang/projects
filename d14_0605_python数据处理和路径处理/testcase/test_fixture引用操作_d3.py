import pytest
from d2_pytest夹具 import setup_and_teardown

# 测试任务：登录功能
def login(username, password):
    if not username or not password:
        return "用户名或密码不能为空"
    elif username == "admin" and password == "12345":
        return "登录成功"
    else:
        return "登录失败"

@pytest.fixture(scope='class')
def setup_and_teardown():
    print('打开浏览器...')
    yield
    print('关闭浏览器...')
# 列表嵌套字典---推荐（可读性高，不会受数据增加或者减少影响）
case_data = [{'caseid':1,'标题':'数据正确，登录成功','用户名':'admin','密码':'12345','期望结果':'登录成功'},
             {'caseid':2,'用户名':'admin','密码':'122222','期望结果':'登录失败'},
             {'caseid':3,'用户名':'','密码':'12345','期望结果':'用户名或密码不能为空'},
             {'caseid':4,'用户名':'admin','密码':'','期望结果':'用户名或密码不能为空'}]

# 第二步：用数据去驱动1个用例进行多次执行
class TestLogin:
    @pytest.mark.parametrize('item',case_data)
    def testlogin_1(self,item,setup_and_teardown): #item：接受测试数据 #setup_and_teardown:调用夹具
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

def test_aa(): # 这条用例不会使用夹具中的前置和后置，因为没有调用夹具
    assert 1 == 1

