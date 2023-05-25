# 题目1：
# 把以下字典分行添加到文件当中：
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
# 得到一个 info.txt 的文件：
# name,age,gender,hobby,motto
# 明鹏程,22,男,学习, 学习使我快乐
# 萌笑天,20,女,拿30K offer,下次拿个40K 的
#
# with open(file = "info.txt", mode = "w",encoding = "utf-8") as f:
#     # 写入表头
#     f.write("name,age,gender,hobby,motto\n")
#     # 写入数据
#     for info in person_info:
#         f.write("{},{},{},{},{}\n".format(info["name"], info["age"], info["gender"], info["hobby"], info["motto"]))


#
# 题目2：
# 手工准备cases.txt 文件，文件中手工复制 2 行数据：
# url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:/futureloan/mvc/api/member/recharge@mobile:18866668888@pwd:1000
# 请利用上课所学知识，把txt里面的两行内容取出然后保存到一个列表和字典当中：（可定义函数）
# 列表当中，有2个字典
# 每一行的数据，就是一个字典。
# 字典的key分别是：url,mobile,pwd
file_path = r'D:\office\Python\projects\d8_0522_python文件处理和导包操作\info.txt'
# with open(file = file,mode='r',encoding='utf-8') as f:
#     print(f.read())
#     file1 = list(f.read())

def read_case_from_file(file_path):
    case=[]
    with open(file_path,"r") as f:
        for line in f:
            line = line.strip()
            print(line)
            items = line.split('@')
            print(items)
            case_dict = {}
            for item in items:
                key,value = item.split(':')
                case_dict[key] = value
            case.append(case_dict)
        return case
cases = read_case_from_file(file_path)
print(cases)


