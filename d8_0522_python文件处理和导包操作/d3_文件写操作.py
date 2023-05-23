'''
 - 1、打开文件：file = open()
    - 2、操作：
      - 读操作
      - 写操作
    - 3、关闭文件：file.close()
'''
# 位置传值
file = r'D:\office\Python\projects\d8_0522_python文件处理和导包操作\test.log'
# 1-打开文件
# myfile2 = open(file = file,mode='a',encoding='utf-8')
myfile2 = open(file = file,mode='w',encoding='utf-8')

# 2- 写入内容到文件
myfile2.write('1234567\n')
myfile2.write('今天是星期一')

# 3-关闭文件
myfile2.close()