''''''
'''
  - 字典常见的操作：查看、增加键值对、删除键值对、修改键值对
  - 1）查看
    - 方式一：字典名[key]
    - 方式二：字典名.get(key)
'''
# actor = {# key-键         value-值
#     "最喜欢的影视剧演员":['胡歌','吴彦祖','梁朝伟'],
#     "最喜欢的歌手":['林俊杰','萧敬腾','周杰伦'],
#     "最喜欢的喜剧明星":['沈腾','小岳岳']
# }
# # singer = actor["最喜欢的歌手"]
# # print(singer)
# # print(actor['abc']) # key不存在的时候，会报错KeyError: 'abc'
#
# print(actor.get('最喜欢的喜剧明星'))
# # 获取最喜欢喜剧明星中的最后一个明星  ---列表取值
# print(actor.get('最喜欢的喜剧明星')[-1])
#
# print(actor.get('abc'))  # key不存的时候，不会报错，默认返回None
# print(actor.get('abc','key不存在'))  # key不存的时候，返回设置的默认值
# print(actor.get('最喜欢的喜剧明星','key不存在'))  # key存在，则返回key后的value值


'''  - 2）增加
    - 字典名[不存在的key] = 新的值
  - 3）修改
    - 字典名[key] = 新的值'''

# week = {
#     1:'周一',
#     2:'周二',
#     3:'周五',
#     (6,7):['周六','周天']
# }
# # 修改：'周五' ==》周三
# week[3] = '周三'
# print(week)
#
# # 增加：4:'周四'
# week[4] = '周四'
# print(week)


'''  - 4)删除
    - 字典名.popitem()   ----删除最后一个键值对
    - 字典名.pop(key)    ---删除指定的键值对
    - 字典名.clear()    ---清空
'''
info = {
    '姓名':'lemon',
    '年龄':18,
    '地址':'湖南长沙'
}
# info.popitem()
# print(info)

# info.pop('年龄')
# print(info)
# info.pop('abd')  # key不存在，则会报错KeyError: 'abd'
# print(info)

# info.clear()
# print(info)
