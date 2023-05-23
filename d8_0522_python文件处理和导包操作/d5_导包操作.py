# test和当前的py文件在同一级目录下
# import test
# print(test.a)
# test.fun1()

# test和当前的py文件在同一级目录下
from test import fun1,a
fun1()
print(a)


# test和当前的py文件在不在同一级目录下----建议从项目目录去开始找
from d8_0522_python文件处理和导包操作.d1.test2 import fun1,a
fun1()
print(a)
# test和当前的py文件在不在同一级目录下----建议从项目目录去开始找
from d8_0522_python文件处理和导包操作.d1 import test2
test2.fun1()
print(test2.a)



# 自带的库文件(库)
# 导入文件
import keyword
print(keyword.kwlist) # 文件.变量

# 导入方法
from random import randint
print(randint(1,10)) # 方法()

# 导入文件
import time
time.sleep(2) # 文件.方法()

# 导入方法
from time import sleep as sl  # 取个别名
# sleep(2) # 方法()
sl(2)  # 使用别名来调用