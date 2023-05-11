''''''
'''- 1、字符串类型(str)基本定义
  - 特点：凡是用引号(单、双、三)引起来的值，就是字符串
  - 关键字：str
  - 类型：type()
  - 长度：len()  ---引号里面内容都会占长度，空格也会占长度
'''
# s = ' hello py61 '
# s = '10'
# s = "True"
# s = '''hello world'''
# s = """hello python"""
# s = ''  # 空字符
# print(type(s),len(s))


'''2-字符串的转义'''
# s1 = '\a\b\c\d\e\f\ghijklm\n\51\890684'
s2 = '\\a\\b\c\d\e\\f\ghijklm\\n\\51\890684'
print(s2)

# s3 = r'\a\b\c\d\e\f\ghijklm\n\51\890684'
s3 = R'\a\b\c\d\e\f\ghijklm\n\51\890684'
print(s3)

file = r'D:\Pycharm_workspace\a\note\apy61'
print(file)

# 第一种：单双嵌套使用    我爱"python"
# sstr = '我爱"python"'
# sstr2 = "我'爱'python"
# print(sstr)
# print(sstr2)

# 第二种：斜杠来转义
sstr = "我爱\"python\""
print(sstr)

# 第三种：三引号引起来
# sstr = '''我爱"python"'''
# print(sstr)
sstr = """我爱"python",你呢？"""
print(sstr)



