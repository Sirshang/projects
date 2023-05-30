from loguru import  logger

logger.add(sink = 'test_login.log',
           level='INFO',
           rotation='1day',
           # rotation='10Mb',
            compression='zip')

logger.info('开始执行...')
username = input('请输入用户名：')
passwd = input('请输入密码：')
logger.info(f'输入数据，用户名：{username}，密码：{passwd}')
if username == 'admin' and passwd == '123456':
    print('登录成功')
    logger.info('登录成功')
else:
    print('登录失败')
    logger.error('登录失败')