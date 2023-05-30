

# class Car:
#     have_whell = True
#     def __init__(self):
#         self.color = '白色'
#         self.brand = 'BYD'

# - 1)获取实例属性 ---频率是最高
#   - 方式一：对象名.实例属性名
#   - tips：实例属性是不能通过类名.实例属性名的方式去获取，会直接报错，只能通过对象名.实例属性名

# - 2)修改实例属性
#   - 对象名.实例属性名 = 新的值
# mycar = Car()
# mycar.color = '红色'
# print(mycar.color)
#
# yourcar = Car()
# print(yourcar.color)

# - 3)添加实例属性
#   - 对象名.不存在实例属性名 = 新的值
# mycar = Car()
# mycar.seat = '4座'
# print(mycar.seat)
# 会报错，不会影响其他对象
# print(yourcar.seat)

# - 4)删除实例属性
#   - hasattr(对象名,'实例属性'):判断对象是否有指定的实例属性，有这个属性就返回True,否则返回False
#   - getattr(对象名,'实例属性',默认值): ---频率最高的
#   - setattr():
#     - 修改类属性值：setattr(对象名,'实例属性','修改后的值')
#     - 增加类属性值：setattr(对象名,'实例属性','新增的属性值')
#   - delattr(对象名,'实例属性'):

class Car:
    have_whell = True
    def __init__(self):
        self.color = '白色'
        self.brand = 'BYD'

mycar = Car()
if hasattr(mycar,'color'):
    # print(getattr(mycar,'color'))
    delattr(mycar,'color')
else:
    print(setattr(mycar,'color','黑色'))
# 查看属性值
print(getattr(mycar, 'color','aaa'))

yourcar = Car()
print(getattr(yourcar, 'color'))