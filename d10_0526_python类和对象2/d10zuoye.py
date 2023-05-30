# 题目1：封装一个学员类StudentStudy
# 属性：姓名，年龄、所在城市、期望薪资
# 方法一：打印学员正在学习的课程，课程作为参数传递。  XXX学员正在学习XXX课程
# 方法二：打印学员的期望薪资。XXX学员学完后的期望薪资为XXX
# 实例化2个学员，分别调用方法一和方法二

# class StudentStudy:
#     def __init__(self, name, age, city, sal):
#         self.name = name
#         self.name = age
#         self.name = city
#         self.sal = sal
#
#     def study(self,course):
#         print(f'{self.name}学员正在学习{course}课程')
#         self.expected_salary()
#
#     def expected_salary(self):
#         print(f'{self.name}学员学完后的期望薪资为{self.sal}')
#
# A = StudentStudy('张三', 30, '北京', '15k')
# A.study('Python')
# print(A)



#
# 题目2:
# 封装一个员工类Employee:
# 属性：员工姓名、工作年限、户籍城市、薪资、岗位名称
# 方法一：计算员工的一年薪资总额(不用含年终奖)
# 方法二：打印员工的姓名和工作年限： 员工XXX 工作年限为 XX
#              (通过self访问员工名字和员工工作年限)
# 实例化2个员工，分别调用方法一(打印员工的年度薪资总额)和方法二
# class Employee:
#     def __init__(self, name, years_of_service, hometown, salary, position):
#         self.name = name
#         self.years_of_service = years_of_service
#         self.hometown = hometown
#         self.salary = salary
#         self.position = position
#
#     def annual_salary(self):
#         return self.salary * 12
#
#     def print_info(self):
#         print(f"员工{self.name}工作年限为{self.years_of_service}年")
#
# employee1 = Employee("张三", 5, "北京", 10000, "工程师")
# employee2 = Employee("李四", 3, "上海", 8000, "产品经理")
#
# print(f"{employee1.name}的年度薪资总额为{employee1.annual_salary()}元")
# print(f"{employee2.name}的年度薪资总额为{employee2.annual_salary()}元")
#
# employee1.print_info()
# employee2.print_info()

# 题目3:
# 封装一个学生类Student， -
# 属性：姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
# 方法一：计算总分，
# 方法二：计算三科平均分
# 方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx,性别：xxx。
# 请定义此类，并实例化2个学生,并打印每个学生的个人信息，计算总分、计算平均分！
# class Student:
#     def __init__(self,name,sex,age,english_sore,math_sore,chinese_sore):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.english_sore = english_sore
#         self.math_sore = math_sore
#         self.chinese_sore = chinese_sore
#
#     def sum_avg(self):
#         total_score = self.english_sore + self.math_sore + self.chinese_sore
#         avg_score = total_score / 3
#         return total_score, avg_score
#     def student_info(self):
#         total_score, avg_score = self.sum_avg()
#         print(f"我的名字叫{self.name}，年龄：{self.age},性别：{self.sex},计算总分{total_score}、计算平均分{avg_score}")
#
# student1 = Student("张三", "男","20", 100, 100,100)
# student2 = Student("李四", "男","20", 200, 100,100)
#
# score1 = student1.sum_avg()
# score2 = student2.sum_avg()
# print(score1)
# print(score2)
# student1.student_info()
# student2.student_info()

# 题目4:
# 编写一个工具箱类和工具类
# 工具类：需要有工具具的名称、功能描述、价格。
# 工具箱类：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
# 实例化几个工具。并在工具箱对象当中做添加/删除/查看工具操作，获取工具箱对象中有几个工具。
# 工具比如锤子、斧头、螺丝刀等工具。
# 提示：不需要用到继承。

# class Tool:
#     def __init__(self, name, description, price):
#         self.name = name
#         self.description = description
#         self.price = price
#
# class Toolbox:
#     def __init__(self):
#         self.tools = []
#
#     def add_tool(self, tool):
#         self.tools.append(tool)
#
#     def remove_tool(self, tool):
#         if tool in self.tools:
#             self.tools.remove(tool)
#         else:
#             print(f"{tool.name}不在工具箱中")
#
#     def view_tools(self):
#         if len(self.tools) == 0:
#             print("工具箱中没有工具")
#         else:
#             for tool in self.tools:
#                 print(f"{tool.name}：{tool.description}，价格：{tool.price}元")
#
#     def get_tool_count(self):
#         return len(self.tools)
#
# hammer = Tool("锤子", "敲打物品", 50)
# axe = Tool("斧头", "砍伐木材", 80)
# screwdriver = Tool("螺丝刀", "拧紧螺丝", 20)
#
# toolbox = Toolbox()
# toolbox.add_tool(hammer)
# toolbox.add_tool(axe)
# toolbox.add_tool(screwdriver)
#
# toolbox.view_tools()
# print(f"工具箱中有{toolbox.get_tool_count()}个工具")
#
# toolbox.remove_tool(axe)
# toolbox.view_tools()
# print(f"工具箱中有{toolbox.get_tool_count()}个工具")
#
# toolbox.remove_tool(axe)
# print(f"工具箱中有{toolbox.get_tool_count()}个工具")