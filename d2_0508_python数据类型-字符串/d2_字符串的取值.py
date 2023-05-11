'''字符串取值
1-单个字符：字符串名[索引值]
'''
# s = 'hello py61'
# print(s[0])
# print(s[-1])
# print(s[9])
# print(len(s))
# print(len(s)-1)
# print(s[10])  # 索引值超过字符串的长度，报错IndexError: string index out of range

'''字符串取值
2-多个字符：字符串名[start:end]
'''
s = 'hello py610'
# print(s[0:3])  # hel
# print(s[0:5]) # hello
# print(s[0:4]) # hell
#
# print(s[6:]) #py61
# print(s[:3]) #hel

print(s[0::2]) # 2位一组，每组中去第一个
print(s[0:2:3]) #he--->h

print(s[::])  # 默认输出整个字符串
print(s[::-1])

s = 'hello py610'
# print(s[0:3])  # hel
b = '123'
print(b[0::2]) # 12---1  3---3
print(b[0::3])


