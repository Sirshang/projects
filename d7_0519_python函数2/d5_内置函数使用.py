# 1、enumerate()n

# 获取元素以及元素的索引值
lst = ['python','test','mysql']
# for i in lst:
#     print(i)
#     print(lst.index(i))

# for index,value in enumerate(lst):
#     print(index)
#     print(value)

# for i in enumerate(lst):
#     print(i)
#     print(i[0])
#     print(i[1])


# 2、eval()
a = '1 + 1'
# print(a)
# print(eval(a))  # 将字符串的表达式变成表达式来进行结果的计算

# res = input('请输入一个表达式：')
# print(eval(res))

lst_str = '[1,2,3]'
# print(type(lst_str))
# new_lst_str = eval(lst_str)
# print(new_lst_str,type(new_lst_str))
#
# dict_str = "{'name':'lemon'}"
# new_dict_str = eval(dict_str)
# print(new_dict_str,type(new_dict_str))


# import requests
# code_str = '''print(requests.request("get", 'http://testingpai.com/').text)'''
# print(code_str)
# eval(code_str)


# 3、zip()
a = ['编号','用户名','密码']
b = [1,'admin','123456']
 # 数据：{"编号"：1，“用户民”："admin","密码"：’123456‘}
# data = dict(zip(a, b))
# print(data)
#
# new_list_data = tuple(zip(a,b))
# print(new_list_data)

# 测试数据：excel
# 接口自动化操作：读取数据----数据格式处理----接口用例执行
a = [['用例id','标题','用户名','密码','期望结果'],
    [1,'登录成功','test','test123','登录成功，页面跳转到首页'],
    [2,'用户名为空，登录失败','','test123','登录失败，提示用户名不能为空'],
    [3,'密码为空，登录失败','test','','登录失败，提示密码不能为空']
    ]
# [{'id':1,'用户名':'test'},
# {'id':2,'用户名':'test123'}]
# new_data = []
# title = a[0]
# for case in a[1:]: # 去除第一条数据
#     # print(case)
#     new_case = dict(zip(title,case))
#     print(new_case)
#     new_data.append(new_case)
# print(new_data)
new_data=[]
title = a[0]
print(title)
for case in a[1:]:
    # print(case)
    data = dict(zip(title,case))
    print(data)
    new_data.append(data)
print(new_data)


