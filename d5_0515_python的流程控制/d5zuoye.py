# 题目1：
# 一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，
# 会给10%的折扣；如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣和最终价格。
# 输入:
# price = xxx
# 输出:
# 购买折扣：8 折
# 优惠价格：xxx 元

# price = input("请输入购买金额: ")
# price = int(price)
# if price >= 50 and price <= 100:
#     print("会给10%的折扣")
# elif price > 100:
#     print("金额大于100元会给20%折扣")
# else:
#     print("小于50，不打折")
#
# 题目2：闰年判断
# 输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）
# 如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”。
# 闰年：普通年能被4整除且不能被100整除的为闰年，世纪年能被400整除的是闰
#
# year = int(input("请输入年份："))
# if (year % 4 ==0 and year % 100 !=0) or year % 400 ==0:
#     print("是")
# else:
#     print("不是")

# 题目3：求三个整数中的最大值
# 提示：可定义3个变量，然后比大小
# nums = []
# for i in range(3):
#     num = int(input("请输入第"+str(i+1)+"个数："))
#     nums.append(num)
#     nums.sort(reverse=True)
# print(nums)


# 题目4：编写如下程序：
# a.用户输入1 - 7
# 七个数字，分别代表周一到周日；
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
# c.如果输入0，退出循环
# d.输入其他内容，提示：“输入有误，请重新输入！”
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。

# nums = []
# for i in range(7):
#     num = int(input("请输入第"+str(i+1)+"个数："))
#     if num == 1:
#         print("周一")
#     elif num == 2:
#         print("周二")
#     elif num == 3:
#         print("周三")
#     elif num == 4:
#         print("周四")
#     elif num == 5:
#         print("周五")
#     elif num == 6:
#         print("周末")
#     elif num == 7:
#         print("周末")
#     elif num == 0:
#         break
#     else:
#         print("输入有误，请重新输入")


# 题目5：编写程序实现，
# 在程序中预设一个0~9
# 之间的整数(预设就是指自己指定一个数字即可)，让用户通过键盘输入所猜的数，如果大于预设的数，显示“遗憾，太大了”，
# 小于预设的数，显示“遗憾，太小了”，如此循环，直至猜中该数，显示“预测N次，你猜中了！”，其中N是用户输入数字的次数。
# 提示：使用while无限循环，当猜中时break
#
# 题目6：冒泡排序

# def bubble_sort(lst):
#     n = len(lst)
#     for i in range(n):
#         for j in range(n - i - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst

lista = [1,2,7,4,90,60]
for i in range(1,len(lista)):
    # print(i,"+++")
    for x in range(0,len(lista)-i):
        # print(x)
        if lista[x] > lista[x+1]:
            # c = lista[x]
            # lista[x] = lista[x+1]
            # lista[x+1] = c
            lista[x],lista[x+1] = lista[x+1],lista[x]
print(lista)

# 题目7、输出99乘法表(双重for循环)
# 格式如下：（每项数据之间空一个Tab键，可以使用
# "\t"）
#
#
# 题目8：用户输入月份, 判断这个月是哪个季节(for循环实现)
# month = int(input("请输入月份："))
# season = ""
#
# for i in range(1, 13, 3):
#     if month >= i and month <= i+2:
#         if i == 1:
#             season = "冬季"
#         elif i == 4:
#             season = "春季"
#         elif i == 7:
#             season = "夏季"
#         else:
#             season = "秋季"
#         break
#
# print("%d月份属于%s。" % (month, season))