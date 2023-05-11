'''
- 1）查看
    - 列表中每个元素都是有索引值，索引值的编号方式和字符串是一样的，正序索引，反序索引
    - 获取列表中单个元素语法：列表名[索引值]
    - 获取列表中多个元素语法：列表名[start:end:step]
'''
info = ['小手套','测试工程师',15000,3.5,[13012344321,13399990000]]
#          0        1       2       3       4
# 查看薪资
sal = info[2]
print(sal,type(sal))

# 查看薪资和年限
sal_year = info[2:4:1]
# sal_year = info[2:4:]
print(sal_year)

# 13399990000的手机号码
# 分步写
phone = info[-1]
print(phone)
phone1 = phone[-1]
print(phone1)
# 合起来写
phone2 = info[-1][-1]
print(phone2)

print(info[::-1])




