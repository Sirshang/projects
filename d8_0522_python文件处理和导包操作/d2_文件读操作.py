'''
 - 1、打开文件：file = open()
    - 2、操作：
      - 读操作
      - 写操作
    - 3、关闭文件：file.close()
'''
# 位置传值
file = 'D:\office\Python\projects\d8_0522_python文件处理和导包操作\demo.txt'
# myfile = open(file)
# 指定传值
# 1-打开文件
myfile2 = open(file = file,encoding='utf-8')

# 2- 读取文件内容
all_content = myfile2.read()
print(all_content,type(all_content))

# all_content_lines = myfile2.readlines()
# print(all_content_lines)
# print(all_content_lines[1]) # 读取第二行的内容

# row1 = myfile2.readline()
# print(row1)

# 3-关闭文件
myfile2.close()