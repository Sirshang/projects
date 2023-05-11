# 1、替换
# date = '2023/5/8'
# # new_date = date.replace('/','-')  # 不指定次数，所有都替换
# new_date = date.replace('/','-',1)
# print(new_date)
#
# # 2、分割
# time = '21:38'
# new_time = time.split(':')
# print(new_time)  # 列表中
#
# new_data2 = date.split('/')
# print(new_data2)

# 3、查找
s = 'hello py61'
# idx = s.find('p')
# idx = s.find('z')  # 字符不存在，不会报错，会返回-1
# idx = s.find('py61')  # 多个字符，字符串存在，则返回第一个字符所对应的索引
# idx = s.find('py60')  # 多个字符，字符串不存在，则返回-1
# print(idx)

# # idx1 = s.index(' ')
# idx1 = s.index('z') # 字符不存在，报错：ValueError: substring not found
# print(idx1)


# 4、去除首尾指定字符
# s = '$$$$$$hello $$$$$$ py61@@@@@@'
# new_s = s.strip('$')
# print(new_s)
#
# new_s1 = new_s.strip('@')
# print(new_s1)
#
# s1 = s.replace('$','')
# print(s1)
# s2 = s1.strip('@')
# print(s2)
#

# 5、大小写转换
s = 'hello py61'
new_s = s.upper()
print(new_s)

s = 'HELLO PY61'
new_s = s.lower()
print(new_s)

# 6.字符串纯数字组成
# age = '1.9'
# print(age,type(age))
#
# res = age.isdigit()
# print(res)
#
# # new_age = int(age)
# # print(new_age,type(new_age))
#
# new_age1 = float(age)
# print(new_age1,type(new_age1))
