# # 题目1：封装一个学员类StudentStudy
# # 属性：姓名，年龄、所在城市、期望薪资
# # 方法一：打印学员正在学习的课程，课程作为参数传递。  XXX学员正在学习XXX课程
# # 方法二：打印学员的期望薪资。XXX学员学完后的期望薪资为XXX
# # 实例化2个学员（A/B），分别调用方法一和方法二
#
# # 如何定义属性：类属性？实例属性？
# # 实例对象的取值:是相同的--类属性，不相同的--实例属性
# a = 10
#
# def fun():
#     print(a)
#
#
#
# class StudentStudy:
#     # 类属性
#     a = 10
#     b = 20
#
#     # 构造函数
#     def __init__(self,sname,sage,scity,ssal): # 自定义参数
#         # 实例属性
#         self.name = sname
#         self.age = sage
#         self.city = scity
#         self.sal = ssal
#
#     def test(self):
#         # d = 100
#         # 调用类属性
#         print(StudentStudy.a) # 方式一：类名.类属性名
#         print(self.b) # 方式二：self.类属性名   ---->对象名.类属性名
#         # return d
#
#     # 实例方法
#     def info(self,subject):
#         # res = self.test()
#         # 直接调用实例属性，好处：可以减少参数传递
#         print(f'{self.name}正在学习{subject}')
#         # 调用另一个实例方法
#         # self.excepted_sal()
#
#     def excepted_sal(self):
#         print(f'学员:{self.name},学完后的期望薪资:{self.sal}')
#         return 'abc'
#
#
# # 实例化对象的时候会自动调用构造方法，构造方法中的自定义必备参数，在实例对象时一定要给值
# # 位置传值
# A = StudentStudy('张三',30,'北京','15k')
# # print(A.name)
# # A.info(subject='python自动化课程')
# # StudentStudy.info(subject='python自动化课程')  # 报错，不能用类名去调用实例方法
# # A.excepted_sal()
# # A.test()
# # 指定传值
# B = StudentStudy(sname='李四',sage = 35,scity='杭州',ssal = '16k')
# # print(B.name)
# # res = B.excepted_sal()
# # print(res)
#
