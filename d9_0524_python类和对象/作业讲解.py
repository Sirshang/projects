'''题目1：
把以下字典分行添加到文件当中：
得到一个 info.txt 的文件：
name,age,gender,hobby,motto
明鹏程,22,男,学习, 学习使我快乐
萌笑天,20,女,拿30K offer,下次拿个40K 的
'''
person_info = [
    {
        "name": "明鹏程",
        "age": 22,
        "gender": "男",
        "hobby": "学习",
        "motto": "学习使我快乐"
    },
    {
        "name": "萌笑天",
        "age": 20,
        "gender": "女",
        "hobby": "拿30K offer",
        "motto": "下次拿个40K 的"
    }
]
# with open(file = 'info.txt',mode = 'w',encoding='utf-8') as fs:
#     title = ['name,','age,','gender,','hobby,','motto','\n']
#     # row1 = []
#     # row2 = []
#     fs.writelines(title)
#     for i in person_info:
#         # print(i) # 列表中的元素
#         # print(i.values()) # 每个元素中字典中所有值
#         # 整数值变为字符串
#         i['age']=str(i['age'])    # 修改字典的操作
#         print(i.values())
#         # 针对数据再次处理，加上逗号和换行符号
#         new_data = ','.join(i.values())
#         new_data = new_data + '\n'
#         # print(new_data,type(new_data))
#         fs.write(new_data)

'''题目2：
手工准备cases.txt 文件，文件中手工复制 2 行数据：
url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
url:/futureloan/mvc/api/member/recharge@mobile:18866668888@pwd:1000
请利用上课所学知识，把txt里面的两行内容取出然后保存到一个列表和字典当中：（可定义函数）
列表当中，有2个字典 
每一行的数据，就是一个字典。
字典的key分别是：url,mobile,pwd'''
lst= [{'url':'','mobile':'','pwd':''},{'url':'','mobile':'','pwd':''}]
# 第一步：读取数据---readlines()
# 第二步：数据处理---for...
# 第三步：数据拆解----切割


with open('case.txt','r',encoding='utf-8') as fs:
    data = fs.readlines()
    list_res = []
    for i in data:
        data_all = i.strip()
        data_all = data_all.split('@')
        dict_res = {}
        for j in data_all:
            res = j.split(":")
            # print(res)
            dict_res[res[0]] = res[1]
        print(dict_res)
        list_res.append(dict_res)
    print(list_res)














# with open(file='case.txt') as fs:
#     all_data = fs.readlines()
#     # print(all_data)
#     new_lst = []
#     for row in all_data:
#         # print(row) # 每一行数据
#         res1 = row.split('@')
#         # print(res1) # 每一行数据通过@切割
#         dict_cell = {}
#         for cell in res1:
#             # print(cell) # 切割出来的数据再通过冒号切割
#             res2 = cell.split(':')
#             print(res2)
#             # 将数据转为字典形式存储
#             dict_cell[res2[0]] = res2[1].strip('\n') # 字典新增语法，字典名[不存在key] = 值
#         print(dict_cell)
#         # 将字典加入到列表中去
#         new_lst.append(dict_cell)
#     print(new_lst)
