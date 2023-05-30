def fun2():
    print('fun2普通方法')

class Car:
    # 类属性
    have_whell = True

    # 构造函数:名字固定为__init__,必带参数是self
    def __init__(self):
        # 实例属性
        self.color = '白色'
        self.brand = 'BYD'


    # 实例方法：必带的参数self
    def info(self):
        print('info实例方法')

    # 类方法：必带的参数cls,方法上面一定要有@classmethod的装饰
    @classmethod
    def fun1(cls):
        print('类方法')

    # 静态方法:没有必带的参数，法上面一定要有 @staticmethod的装饰
    @staticmethod
    def fun2():
        print('静态方法')



c1 = Car()
# 类方法可以通过对象名调用，也可以通过类名调用
Car.fun1()
c1.fun1()

# 静态方法调用：通过类和对象都可以调用
Car.fun2()
c1.fun2()
