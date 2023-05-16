'''1-for和if的使用'''

users = ['test','zhagnsan','lisi'] # 已经注册的账号
login_user = ['test','amdin','lemon']  # 要进行登录的账号信息

for user in login_user:
    if user in users:
        print(f'{user}账号已注册，可以进行登录操作')
    else:
        print(f'{user}账号未注册，请写进行注册操作。。。。')


'''2-for+for运用'''
cases_data = [['admin','test123'],
                ['test','123456'],
                ['lemon','lemon123']]
for case in cases_data:
    # print(case)
    for value in case:
        print(value)