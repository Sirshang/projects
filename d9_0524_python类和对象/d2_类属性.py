# 类的定义
# class Car:
#     # 类属性
#     have_wheel = True
#     have_shell = True

'''查看类属性值'''
# # 方式一：对象名.类属性名
# c1 = Car()
# print(c1.have_wheel)
# c2 = Car()
# print(c1.have_shell)
# # 方式二：类名.类属性名
# print(Car.have_shell)

'''修改类属性值'''
# - 方式一：对象名.类属性名 = 新值  ---只是修改自己对象的值
# c1 = Car()
# c1.have_wheel = '有轮子'  # 只是修改自己对象的值
# print(c1.have_wheel)
#
# c2 = Car()
# print(c2.have_wheel) # True
# #   - 方式二：类名.类属性名 = 新值   ---修改了图纸
# Car.have_shell = '有外壳'
# print(Car.have_shell)
# print(c1.have_shell)
# print(c2.have_shell)

'''增加类属性'''
# 方式一：类名.不能存在类属性名 = 新值
# Car.have_system = '有核心系统'
# print(Car.have_system)
# c1 = Car()
# print(c1.have_system)

'''内置方法的使用：
 - hasattr(类名,'类属性'):判断类是否有指定的类属性，有这个属性就返回True,否则返回False
  - getattr(类名,'类属性',默认值):---频率最高的
    - 查看类中类属性的值，如果类属性不存在，可以将默认值输出 
  - setattr():
    - 修改类属性值：setattr(类名,'类属性','修改后的值')
    - 增加类属性值：setattr(类名,'新增类属性','新增的属性值')
  - delattr(类名,'类属性'):删除类中的类属性
'''
class Car:
    # 类属性
    have_wheel = True
    have_shell = True

# getattr(类名,'类属性',默认值):---频率最高的
print(getattr(Car,'have_wheel'))
print(getattr(Car,'have_system','没有have_system类属性值'))  # 好处：不会中断代码，会将默认值输出

# # 需求1：判断Car类是否有have_system属性，如果有则获取这个属性值，如果没有，新增这个属性以及对应的值
# if hasattr(Car,'have_system'):
#     print(Car.have_system)
# else:
#     setattr(Car,'have_system','有核心系统')
# # 获取have_system值
# print(Car.have_system)

# # 需求2：判断Car类是否有have_wheel属性，如果有删除这个属性
# if hasattr(Car,'have_wheel'):
#     delattr(Car,'have_wheel')
# # 获取have_wheel值
# print(Car.have_wheel)


