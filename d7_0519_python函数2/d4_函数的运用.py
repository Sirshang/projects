# 函数中能否调用的其他的函数？
# print(1111)
# # def get_offer(name,sal):
# #     print(f'恭喜{name}同学，获得高薪offer,薪资:{sal}')
# #     eat('奶茶')
#
# def eat(food):
#     print(f'请大家吃{food}')
#
# get_offer('艾良','13k')


print(111)
# 函数能否调用自己本身
def get_offer(name,sal):
    print(f'恭喜{name}同学，获得高薪offer,薪资:{sal}')
    get_offer(name,sal)

get_offer('lemon','15k')

# 扩展：斐波那契数列(递归)
