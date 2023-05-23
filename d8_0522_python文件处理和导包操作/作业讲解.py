'''题目1：定义函数，并通过给函数传递不同的参数(要想清楚哪些做为参数哦！！)：
一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），
如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。
编写一程序，询问购买价，再显示出折扣（%10或20%）和最终价格。'''

def get_price(price):
    if price > 100:
        print(f'消费大于100元，可以享受8折折扣,最终支付金额：{price * 0.8}')
    elif 50 <= price <= 100: # price>=50 and price <= 100
        print(f'消费在50-100元之间，可享受9折折扣，最终支付金额：{price * 0.9}')
    else:
        print(f'消费在50元以下，没有折扣,最终支付金额：{price}')

# get_price(40)


'''题目2：不定长参数
定义函数，将输入的所有数字相乘之后对20取余数，用户输入的数字个数不确定。'''
# def deal(*num): # 元组
#     res = 1
#     for i in num:
#         res = res * i
#     # print(res % 20)
#     return res%20

# print(deal(10,22,33))
# r = deal(10,25,33)
# print(r)

def deal2(**num):  # 字典  {a:10,b:20}
    # print(num)
    # print(num.values())
    res = 1
    for i in num.values():
        res = res * i
    return res % 20

# print(deal2(a = 10,b=20))


'''题目3：列表去重函数
定义一个函数 def remove_element(a_list):，
将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素(不能用集合去重，要使用for循环)'''
# 方式一：集合去重
def fun1(a_list):
    res = set(a_list)  # 集合
    return list(res)
# lst = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# print(fun1(lst))

# 方式二：循环遍历+判断去重
def fun2(a_list):
    new_list = []   # 存储不重复的值
    for i in a_list:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
# lst = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# fun2(lst)


'''题目4：通过定义一个计算器函数，调用函数传递两个参数，
然后获取用户输入，如果用户输入1，对2个参数做加法运算，并返回结果。
如果用户输入2，对2个参数做减法运算，并返回结果。
如果用户输入3，对2个参数做乘法运算，并返回结果。'''
def caculator(num1,num2):
    opearte = input('请输入操作(如：1/2/3):')
    if opearte == '1':
        return num1 + num2
    elif opearte == '2':
        return num1 - num2
    elif opearte == '3':
        return num1 * num2
    else:
        return '操作有误，不支持的操作'

# res = caculator(10,20)
# print(res)


'''题目5：BMI 计算
使用函数完成以下操作
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 : 65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5： 过轻 18.5-25： 正常 25-28： 过重 28-32： 肥胖 高于32： 严重肥胖'''
# height 身高
# weight 体重
def get_bmi(height,weight):
    bmi = weight / height ** 2
    if bmi < 18.5:
        print('过轻')
    elif 18.5 <= bmi <= 25:
        print('正常')
    elif 25 < bmi <= 28:
        print('过重')
    elif 28 < bmi <= 32:
        print('肥胖')
    else:
        print('严重肥胖')

get_bmi(1.62,45)

