# 需求：将列表中的重复元素去除，然后输出结果
lst = [1,2,3,4,5,6,7,1,3,4,5]
# 第一步：转为集合，会自动去重
lst_set = set(lst)
print(lst_set,type(lst_set))
# 第二步：将去重后的集合转为列表
lst = list(lst_set)
print(lst)


# 字典转为集合
info = {
    '姓名':'lemon',
    '年龄':18,
    '地址':'湖南长沙'
}
info_set = set(info)
print(info_set)

info_str = str(info)
print(info_str,type(info_str))  #‘{'姓名': 'lemon', '年龄': 18, '地址': '湖南长沙'}’
print(info,type(info))

# 列表、元组----》字典
# lst = [('name','vance'),('age',20),('tel',13011112222)]
# lst = [['name','vance'],['age',20],['tel',13011112222]]
# lst = ['name','vance','age',20,'tel',13011112222]  # 无法转换，报错，格式不符合要求
# print(dict(lst))

# tpl = (['username','admin'],["password",'123456'])
# tpl = (('username','admin'),("password",'123456'))
# print(dict(tpl))

# 变量去转为字典
res = dict(name = 'kemi',
           addr = '长沙')
print(res)




