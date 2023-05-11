# 元组的定义
name = ('Jennifer','六娃','微笑','学习到两点')
print(name,type(name),len(name))
# 空元组
name1 = ()
print(name1,type(name1),len(name1))
# 元组中只有一个元素，那么一定要在元素后面带上逗号
name2 = ('hello py61',)
print(name2,type(name2),len(name2))

# 元组中元素的查看
# print(name[2])
# print(name[-2])
#
# print(name[:2:])
# print(name[::-1])

# print(name.index('六娃'))
# print(name.index('六娃aaaa')) # 元素不存在，会报错ValueError: tuple.index(x): x not in tuple


# 转换函数
location = ('北纬39°','东经116°')
print('元组转字符串',str(location)) # '('北纬39°','东经116°')'
#需求：增加一个长沙的经纬度，一起放在location存储
# 第一步：转为列表  ---列表可以修改，元组不可以修改
location_list = list(location)
print(location_list)
# 第二步：增加值
location_cs = ['东经111','北纬27']
location_list.extend(location_cs)
print(location_list)
# 第三步：把location_list转为元组
location = tuple(location_list)
print(location)

# 字符串--列表/元组
s = 'hello py61'
# print(list(s))
print(tuple(s))

# 数字（整数、小数、布尔值）不可以转为列表、元组
# num = 10
# print(list(10))  # 报错


