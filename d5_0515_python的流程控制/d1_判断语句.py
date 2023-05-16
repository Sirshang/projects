''''''
'''1-if..else判断
if 条件1:
    条件1满足的时候需要去执行的代码
else:
    条件1不满足的时候需要去执行的代码
'''
# age = int(input('请输入年龄：'))
# if age > 18:
#     print('已经成年了，要负责了...')
# else:
#     print('还未成年....')
# print('hello py61')

'''2-if..elif..else
if 条件1:
    条件1满足的时候需要去执行的代码
elif 条件2:
    条件2满足的时候需要去执行的代码
elif 条件3：
    条件3满足的时候需要去执行的代码
.... 
else:
    所有的条件都不满足的时候需要去执行的代码
'''
# color = input('请输入红绿灯的颜色：')
# if color == '红色':
#     print('红灯停，闯红灯，扣6分')
# elif color == '绿色':
#     print('绿灯行，你正常走了。。。')
# elif color == '黄色':
#     print('黄灯亮了，等一等，不要闯。。。')
# else:
#     print('红绿灯故障，注意观察行车~~')

# 多个if执行的逻辑
# age = 19
# if age > 18:
#     print('a')
# if age >18:
#     print('b')
# else:
#     print('c')


'''3-if判断嵌套使用
if 条件1:
    if 条件2:
       条件1和条件2同时满足时，执行的代码
    else:
       条件1满足，但是条件2不满足时，执行的代码 
else:
    条件1不满足的时候需要去执行的代码
'''
# 需求：用户名为test,密码123456，登录成功，否则提示用户名或密码错误，
# 如果登录的用户名不是test,则提示用户名不存在
# username = input('请输入用户名：')
# passwd = input('请输入密码：')
# 方式一：if嵌套来实现
# if username == 'test':
#     if passwd == '123456':
#         print('登录成功')
#     else:
#         print('用户名或密码错误')
# else:
#     print('用户名不存在~~')

# 方式二：
# if username == 'test' and passwd == '123456':
#     print('登录成功')
# elif username == 'test' and passwd != '123456':
#     print('用户名或密码错误，登录失败')
# elif username != 'test':
#     print('用户名不存在')


# s = 'hello py61'
# if 'h' in s:
#     print('h字符在s变量中')
# else:
#     print('h字符不在s变量中')


# 条件为固定的值
# if False:
#     print('这是if语句')
# else:
#     print('这是else语句')

username = input('请输入用户名：')
print(bool(username))
if username:
    print('用户名不为空，继续判断')
else:
    print('用户名不能为空，请输入用户名！！')