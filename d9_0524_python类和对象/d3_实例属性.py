# 类的定义
class Car:
    # 类属性
    have_wheel = True
    have_shell = True

    # 构造方法
    def __init__(self):
        # 实例属性
        print(self)  # 就是对象本身
        self.color = '白色'
        self.brand = 'BYD'

# - 方式：对象名.实例属性名
print(1111)
c1 = Car()  # 实例化对象的时候，会自调用构造方法
print(c1)
print(c1.color)


