'''
  - 1）增加
    - 列表名.append(值)
    - 列表名.insert(索引值,值)
    - 合并列表：列表1 + 列表2
    - 列表1.extend(列表2)
'''
name = ['Jennifer','六娃','微笑','学习到两点']

# 增加YJ同学姓名到name列表中
# name.append('YJ')
# print(name)

# name.insert(0,'leaf')
# print(name)

new_name = ['YJ','leaf']
# 列表相加后可以得到一个新的列表
# all_name = name + new_name
# print(all_name)

# 将new_name列表加到name列表中去
name.extend(new_name)
print(name)





