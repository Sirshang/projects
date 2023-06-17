import pytest

# 夹具（来实现用例的前置和后置的操作）
@pytest.fixture(scope='class')
def setup_and_teardown():
    print('打开浏览器...')
    yield
    print('关闭浏览器...')

@pytest.fixture
def login_succ():
    print('打开浏览器')
    print('访问网址')
    print('输入用户名、密码')
    print('点击登录')
    yield 'token_value','user_id','user_name'
    print('关闭浏览器')

@pytest.fixture
def order_succ(login_succ): # 调用夹具
    # 支付订单前置
    # print('登录成功')
    print('下单成功')
