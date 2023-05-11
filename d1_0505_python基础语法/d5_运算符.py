''''''
'''- 1、算数运算符：+  -  *  /   //   %'''
# num1 = 10
# num2 = 3
# num2 = 3.1
# num2 = True  # True=1
# num2 = False   # False=0

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)  # 除，和计算器算出来的结果显示一直
# print(num1 // num2) # 整除，
# print(num1 % num2) # 取余数，判断奇数（num % 2 != 0）、偶数（num % 2 == 0）

# 浮点数的运算结果是不准确的
a = 0.1
b = 0.2
print(a + b)
# 了解（扩展）---浮点数计算结果不精确问题的解决方式（金融项目，金额）
from decimal import Decimal
res = Decimal('0.1') + Decimal('0.2')
print(res)


'''2、比较运算符：>  <  >=  <=  ==   !='''
# num1 = 1
# # num2 = 3
# # num2 = 3.2
# num2 = True  #
#
#
# print(num1 > num2)
# print(num1 < num2)
# print(num1 >= num2)
# print(num1 <= num2)
# print(num1 == num2)
# print(num1 != num2)


'''- 5、赋值运算：=  +=  -=  *=  /=  //=  %=
  - 变量的声明就是一种赋值运算符：age = 18
'''
age = 18
age += 2  # age = age + 2
print(age)