'''1-必备参数'''

# 自我介绍：姓名、城市、期望薪资
# 必备参数
def info(name,city,sal):
    print(f'''
    姓名：{name},
    城市：{city},
    期望薪资：{sal}
    ''')
# 位置传值
info('kemi','长沙','12k')
info('Jennifer','北京','15k')
# 指定传值
info(sal='15k',city='湖州',name='六娃')

'''2-缺省参数
当参数中有必备参数、缺省参数，缺省参数一定要放在所有必备参数的后面
'''
# def info(name,city,sal,class_name = 'py61',des='test'):
#     print(f'''
#     姓名：{name},
#     城市：{city},
#     期望薪资：{sal},
#     班级：{class_name}
#     ''')
# # 位置传值
# info('Jennifer','北京','15k')
# info('Jennifer','北京','15k','python61期')
# # 指定传值
# info(sal='15k',city='湖州',name='六娃',class_name = 'py48')


'''3-不定长参数'''
def fun1(*num):
    print(num,type(num))
    # 求和
    # print(sum(num))
    # total = 0
    # for i in num:
    #     total = total + i
    # print(total)
#
#
# # *num不定长参数，只能用位置传值
# fun1()
# fun1(10,20,30)
# fun1(10,20,30,50,70,31859)

# 扩展：解包:元组整体解包成单个元素值
# tpl = (2, 3, 4, 5)  #
# fun1(*tpl)  # ((2,3,4,5),)---->(2,3,4,5)
# fun1(tpl[0],tpl[1],tpl[2],tpl[3])  # 元组的取值



def fun2(**num):
    # print(num,type(num))  # {key:value}
    # 求和
    total = 0
    for i in num.values():
        total  = total + i
    print(total)

# **num不定长参数，只能指定传值
# fun2()
# fun2(a = 10, b = 20 ,num3 = 50)
# fun2(a = 10, num3 = 50)

# 字典解包：
# dit = {'num1':10,'num2':20}
# # fun2(**dit)
# fun2(a=dit['num1'],b=dit['num2'])  # 字典取值



# 扩展：
# a,*b = 1,2,3,4,5,6
# print(a)
# print(b)



