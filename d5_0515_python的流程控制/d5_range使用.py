print(tuple(range(1,10,1)))
print(list(range(10,0,-1)))
print(set(range(10)))


# 用来做遍历，有序数据类型，不能遍历字典和集合，因为字典和集合是无序的，没有索引的
s = 'hello h1aga fgaga '
for i in range(len(s)): # 用range去生成数据的索引的序列
    # print(i)
    print(s[i]) # 通过索引的取值来遍历字符串，字符串名[索引值]


# 用来控制循环的次数
for i in range(100): # [0,1,2,3...99]
    print('hello py61',i)
