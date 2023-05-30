# 方式一：try..except
# try:
#     d = {'a':1,'b':2}
#     # print(d['test'])
#     print(d['a'])
# except: # 可以捕获任何系统异常
#     print('出现异常，请及时处理.....')
# print(123)
# print('py61')

# 方式二：try..except..except..
# try:
#     l = [1,2,3,4,5]
#     # print(l[100])  # IndexError异常出现，直接中断代码
#     print(l[0])
#
#     class Person:
#         pass
#
#     p1 = Person()
#     print(p1.name)  # AttributeError
# except IndexError:
#     print('处理1：超出了范围...')
# except AttributeError:
#     print('处理1：增加实例属性')
#     setattr(p1,'name','py61')
#     print(p1.name)
#
# print(123)

# 方式三：try..except Exception as e
# try:
#     print(d)
# except Exception as e: # 可以捕获任何系统异常,获取异常提示信息
#     print(f'出现异常{e}，请及时处理.....')
# print(123)
# print('py61')

# print(a)


# 抛出异常：语法：raise 系统异常
actual = eval(input('输入表达式：'))
excepted = 2  # 预期结果
# 断言方式一：
if actual ==  excepted:
    print('通过')
else:
    print('失败')
    raise AssertionError  # 手动抛出断言异常，把用例结果置为失败

# 断言方式二：没有任何信息输出就表示断言成功，抛出AssertionError意味着断言失败
assert actual ==  excepted    # 自动化中常用的断言方式

# 两者的区别：结合pytest框架进行报告生成，报告中如何将用例执行结果修改为失败（捕获AssertionError）
# if..else断言：无论走哪个分支，用例的结果都是通过的,通过在失败的分支中加上一个raise AssertionError就可以解决这个问题
# assert断言：断言成功，记录用例为通过，断言失败记录用例为失败



