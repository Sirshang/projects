
a = 10

def fun1():
    # b = 20
    global a
    a = a + 1  # 在函数体中不允许随意去修改全局变量的值
    print(a)
    # print(b)  # 可以使用，b是局部变量，可以在局部使用
    # return b

fun1()
# print(b)  # 报错，b是局部变量，只能在函数内使用

# 在函数外面，要去使用fun1中定义的局部变量b，如何获取？---解决方法，通过return返回出去
# res = fun1()
# print(res)
