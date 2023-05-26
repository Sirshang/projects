'''判断循环作业'''
'''题目1：一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），
如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣；
如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣和最终价格。
输入:price = xxx
输出:购买折扣：8 折,优惠价格：xxx 元'''

# price = input('请输入购买金额：')
# if price.isdigit(): # 判断字符串是否由纯数字组成
#     price = int(price)
#     # 计算最终价格
#     # final_price = 0
#     if price > 100:
#         # final_price = price * 0.8
#         print(f'消费大于100元，可以享受8折折扣,最终支付金额：{price * 0.8}')
#     elif 50 <= price <= 100: # price>=50 and price <= 100
#         # final_price = price * 0.9
#         print(f'消费在50-100元之间，可享受9折折扣，最终支付金额：{price * 0.9}')
#     else:
#         # final_price = price
#         print(f'消费在50元以下，没有折扣,最终支付金额：{price}')
# else:
#     print('请输入整数！！')


'''题目2：闰年判断
输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）
如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”。
闰年：普通年能被4整除且不能被100整除的为闰年，世纪年能被400整除的是闰年'''

# year = int(input('请输入年份（如：2019）：'))
# if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#     print(f'{year}是闰年')
# else:
#     print(f'{year}不是闰年')


'''题目3：求三个整数中的最大值
提示：可定义3个变量，然后比大小'''
# a = int(input('请输入第一个整数：'))
# b = int(input('请输入第二个整数：'))
# c = int(input('请输入第三个整数：'))
# 方式一：假设a就是最大的数字，每次把最大值给到max
# max = a
# if a < b:
#     max = b
# if max < c:
#     max = c
# print(f'输入值为：{a}，{b}，{c}，最大值为：{max}')

# 方式二：三个数依次比较
# if a > b:
#     if a > c:
#         print(f'输入值为：{a}，{b}，{c}，最大值为：{a}')
#     else:
#         # a > b,c > a
#         print(f'输入值为：{a}，{b}，{c}，最大值为：{c}')
# else: # b > a
#     if b > c:
#         print(f'输入值为：{a}，{b}，{c}，最大值为：{b}')
#     else:#b > a， c > b
#         print(f'输入值为：{a}，{b}，{c}，最大值为：{c}')

'''4、周末判断 while+if'''
# 方式一：列表存储周一~周末，然后再做循环+判断
# weekday = ["周一", "周二","周三","周四","周五","周六","周末"]
# #           0        1      2   3       4       5   6
# weekday = {1:'周一',
#            2:'周二',
#            3:'周三',
#            4:'周四',
#            5:'周五',
#            6:'周六',
#            7:'周末'}
# while True:
#     num = input("请输入1-7七个数字，分别代表周一到周日：")
#     if num == "0": # 如果为0就退出循环
#         break
#     if int(num) in range(1,8): # [1,2,3,4,5,6,7]
#         # print(weekday[int(num) - 1])  # 数字正确，则从列表获取值
#         print(weekday[int(num)])  # 数字正确，从字典中获取值
#     else:
#         print("输入有误，请重新输入！")

# 方式二：字典存储值，然后再做循环+判断来
# dict = {1: '周一', 2: '周二', 3: '周三', 4: '周四', 5: '周五', 6: '周六', 7: '周末'}
# while True:
#     num = int(input("请输入1-7七个数字，分别代表周一到周日："))
#     if num in dict.keys():  # 判断输入的值是否在字典的key中 -- [(1,2,3,4,5,6,7)]
#         print(dict[num])  # 在key中就输出对应的周几值
#     elif num == 0:  # 如果输入值等于0，就退出循环
#         break
#     else:  # 如果不是1-7的值，就提示错误
#         print('输入有误，请重新输入！')

'''5、猜数字'''
# num = 5   # 需要猜中的数字
# import random
# num = random.randint(1,100) # 生成一个1-10的随机整数
# print(num)

# count = 0  # 统计猜的次数
# while True:
#     user_num = input("请输入任意数字:")
#     count += 1
#     if int(user_num) > num:
#         print("遗憾，太大了")
#     elif int(user_num) < num:
#         print("遗憾，太小了")
#     else:
#         print("预测{}次，你猜中了！".format(count))
#         break


'''6、冒泡排序：  --算法~~
冒泡排序视频讲解：https://www.bilibili.com/video/BV1JA4y1R78q/?spm_id_from=trigger_reload&vd_source=28cccb26c807f4a9f73f9c60f758cfd4

假设有5个数进行冒泡排序：
    从小到大排列(升序)：如果大于就交换，谁高就交换
    从大到小排列（降序）：如果小于就交换，谁矮就交换
规律：
1、比较几轮？  ---》4轮   规律：i = 数字的个数-1  ----for
2、每轮比较几次？   
    ---》第一轮   4次  ===规律：次数(j) =  数字个数- 比较的轮数(i)  --for
    ---》第二轮   3次
    ---》第三轮   2次
    ---》第四轮   1次
规律：
    比较轮次规律：i = len()-1
    每轮比较次数规律：len() - i
口诀：
    N个数字来排序
    外层循环i = N-1  ----》  range(1,len(a))
    内层循环j = N-i    ----> ragne(len(a) - i )
    升序排列：a[j] > a[j+i] ---做交换
    降序排列：a[j] < a[j+i] ---做交换
'''
# a = [11,22,1,23,88,12,185,90]
# # 比较轮次
# for i in range(1,len(a)):
#     # print('轮次')
#     for j in range(len(a)-i):
#         # print('次数')
#         # print(j)
#         if a[j] < a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)

# a = 1
# b = 2
# a,b = b,a # 值交换


'''7、99乘法表
行数：9行   
列数：
    第一行  1列
    第二行  2列
    第三行  3列
    ...
    第九行  9列
'''
# # 方式一：先打出一个正方形，然后再取需要显示的值
# lst = [1,2,3,4,5,6,7,8,9]
# for i in lst:
#     for j in lst:
#         if j <= i:
#             print(f'{j} * {i} = {i * j}',end = '\t')
#     print()

# 方式二：找出行、列的规律，通过双重for循环来控制
# for i in range(1,10): # i=[1,2,3,4,5,6,7,8,9]
#     # print('行数', i)
#     for j in range(1,i+1): #根据i的取值而变化，i=1,j=[1]; i=2,j=[1,2];i=3,j=[1,2,3]...
#         # print('列数',j,end = '\t')
#         print(f'{j} * {i} = {i * j}',end = '\t')
#     # 打完每一行的所有列之后做换行操作
#     print()


'''8、季节判断'''
# season = {
#     '春季' : [1,2,3],
#     '夏季' : [4,5,6],
#     '秋季' : [7,8,9],
#     '冬季' : [10,11,12]
# }
# month = input('请输入月份（1-12）:')
# if month.isdigit(): # 字符串是否由纯数字组成
#     month = int(month)
#     if  1 <= month <= 12:
#         for s,m in season.items(): # s = '春季'  m = [1,2,3]
#             if month in m:
#                 print(f'{month}月是{s}')
#                 break;
#     else:
#        print('非法输入！')
# else:
#     print('非法输入！')







