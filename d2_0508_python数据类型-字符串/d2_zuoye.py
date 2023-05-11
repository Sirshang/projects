# 作业提交形式：py文件。每一题请带上题目，再是代码。一定要代码执行成功之后，再上交py文件。
#
# 基础必做题：
# 题目1：
# 现在有字符串：str1 = 'python cainiao 666'
# 请使用代码找出第5个字符
# 请复制一份字符串，保存在变量str_two中(赋值运算符)
#
# str1 = 'python cainiao 666'
# print(str1[4])
#
# str_two= str1

# 题目2：
# 卖橘子的计算器（字符串转化）
# 写一段代码，用户输入橘子的价格，和重量，计算出应该支付的金额！（
# 提示：不需要校验数据，默认传入数字就可以了。
# 使用input函数获取用户输入哦，并且input得到的数据都是字符串类型）
#
# price = input("请输入橘子价格：")
# weight = input("请输入橘子重量：")
# num = float(price)*float(weight)
# print("应该支付金额:",num)
#
# 题目3：
# 字符串综合演练 （字符串索引和切片。注意位置和索引的区别）
# my_hobby = "Never stop learning!"
#
# 说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”）；
# “索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）；
# 开始位置 ，是指字符串起始，即下标为0开始；末尾，是指字符串最后。
#
# my_hobby = "Never stop learning!"
# 1）截取从 位置2 ~ 位置6 的字符串(含 位置2和6)
# s = my_hobby[1: 5]

# 2）截取完整的字符串
# s = my_hobby[::]
# print(s)
# 3）从 索引3 开始，每2个字符中取一个字符(含索引3，步长为2)
# s = my_hobby[3::2]
# print(s)
# 4）截取字符串末尾两个字符
# s = my_hobby[-2:]
# print(s)
# 5）字符串的倒序
# s = my_hobby[-1::-1]
# print(s)
#
# 题目4：
# 有字符串s如下
# s = 'python'
# 请编写代码打印字符串s的第一个字符
# 请编写代码打印字符串s的最后一个字符
# s = 'python'
# print(s[0])
# print(s[-1])

# 题目5：
# 有字符串s如下
# s1 = '1234567890'
# 请编写代码用切片的方式打印出
# '13579'
# print(s[0::2])
# 请编写代码用切片的方式打印出

# print(s1[-2:-11:-2])
# 请编写代码用切片的方式打印出
# '24680'
# print(s[1::2])
# (找出数字规律。确认起始索引、结束索引、步长。确定是正序切片还是倒序切片)
#
# 题目6
# 将"hello world"转为全部字母大写"HELLO WORLD"
# s = "hello world"
# new_s = s.upper()
# print(new_s)
#
# 题目7
# 将字符串"I Love Java" 变成"I Love Python"（替换）
#
# s = "I Love Java"
# print(s.replace("Java", "Python"))
# 题目8
# 字符串格式化
# 把姓名、年龄、密码、性别、专业、爱好分别存储在变量中，用下列格式展示：
# age = 18
# 控制台中输出的显示效果：
#
# -------------------------------
# 姓名：xxx
# 年龄：xxx
# 密码：xxx
# 性别：xxx
# 专业：xxx
# 爱好：xxx
# -------------------------------
# name = '张三'
# age = 18
# password = '123456'
# gender = '男'
# major = '计算机科学与技术'
# hobby = '打篮球、听音乐'
# print('------------------------------')
# print('姓名：{}'.format(name))
# print('年龄：{}'.format(age))
# print('密码：{}'.format(password))
# print('性别：{}'.format(gender))
# print('专业：{}'.format(major))
# print('爱好：{}'.format(hobby))
# print('------------------------------')

#
# 题目9：下面字符串定义正确的结果是（多选）ABC
# A.
# 'hello world!'
# B.
# "hello world!"
# C.
# '他说："他很努力！"'
# D.
# """窗前明月光，疑是地上霜。
# 举头望明月，低头思故乡。"""
#
# 题目10：编写代码打印100个 * (使用字符串的 * 运算符)
# for i in range(100):
#     print('*')
#
# 题目11：下面的变量s是字符串形式的电话
# s = '010-888-888-888'
# # 请编写代码使用字符串方法去掉s中的'-'
# s1 = s.replace("-", "")
# print(s1)
#
# 二 、 挑战级选做题(可交可不交)：
#
# 题目12：将字符串中的单词位置反转
# "hello xiao mi"
# 转换为
# "mi xiao hello"
s = "hello xiao mi"
words = s.split()  # 将字符串按空格分割成单词列表
print(words)
words.reverse()  # 反转单词列表

result = ' '.join(words)  # 将反转后的单词列表合并成字符串
print(result)
# （提示：通过字符串分割，拼接，列表反序等知识点来实现）
#
#
# 题目13：以下哪个是正确的字符串（）（多选）
# A
# 'abc"ab"
# B
# 'abc"ab'
# C
# "abc"
# ab
# "
# D
# "abc\"ab"
#
# 题目14："ab" + "c" * 2
# 结果是：（）
# A
# abc2
# B
# abcabc
# C
# abcc
# D
# ababcc