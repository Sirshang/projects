class Car:
    have_whell = True
    def __init__(self):
        self.color = '白色'
        self.brand = 'BYD'

    def fast(self):
        print('加速')

    def slow(self):
        print('减速')

    def music(self):
        print('播放音乐')

class Test:
   pass

class AutoCar(Car,Test):  # 可以继承多个类
    # 实例方法
    def auto_driver(self):
        # 调用父类的方法
        self.fast()
        self.slow()

a1 = AutoCar()
# 继承了Car类，可以直接使用父类中的属性和方法
a1.fast()
print(a1.have_whell)
# print(a1.color)
# a1.auto_driver()


# 爷爷--爸爸--儿子继承关系:传递关系
# class A:
#     def fun1(self):
#         print('A类的fun1方法')
#
# class B(A):
#     def fun2(self):
#         print('B类的fun2方法')
#
# class C(B):
#     pass
#
# c1 = C()
# c1.fun2()
# c1.fun1()
