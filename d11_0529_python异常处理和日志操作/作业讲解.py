# 第一题 学员类StudentStudy
class StudentStudy:
    def __init__(self,name,sex,city,want_salary):
        self.name = name
        self.sex = sex
        self.city = city
        self.want_salary = want_salary

    def print_studing_course(self,course_name):
        print("{}学员正在学习{}课程".format(self.name, course_name))

    def print_wanted_salary(self):
        print("{}学员学习完后的期望薪资为{}".format(self.name, self.want_salary))

# 学生1
# zs = StudentStudy("zs", "男", "长沙"  , 14000)
# zs.print_studing_course("python自动化")
# zs.print_wanted_salary()
# 学生2
# lisa = StudentStudy("lisa", "女", "深圳", 40000)
# lisa.print_studing_course("python测开")
# lisa.print_wanted_salary()


# 第二题 员工类Employee
'''题目2:
封装一个员工类Employee:
属性：员工姓名、工作年限、户籍城市、薪资、岗位名称  ---实例属性
方法一：计算员工的一年薪资总额(不用含年终奖)
方法二：打印员工的姓名和工作年限： 员工XXX 工作年限为 XX
             (通过self访问员工名字和员工工作年限)
实例化2个员工，分别调用方法一(打印员工的年度薪资总额)和方法二  '''

class Employee:
    def __init__(self,sname,syear,scity,ssal,sjob):
        self.name = sname
        self.year = syear
        self.city = scity
        self.sal = ssal
        self.job = sjob

    def all_sal(self):
        tatal_sal = self.sal * 12
        return tatal_sal

    def info(self):
        print(f'员工{self.name}工作年限为{self.year}')
# e1 = Employee('员工1',3,'北京',15000,'测试')
# print(e1.all_sal())
# e1.info()
#
# e2 = Employee('员工2',1,'北京',1000,'运维')
# sal = e2.all_sal()
# print(sal)
# e2.info()


# 第三题 学生类Student
class Student:
    def __init__(self,name,age, sex, en_score, math_score, cn_score):
        self.name = name
        self.age = age
        self.sex = sex
        self.en_score = en_score
        self.math_score = math_score
        self.cn_score = cn_score

    def get_all_scores(self):
        '''获取总分'''
        sum = self.en_score + self.math_score + self.cn_score
        return sum

    def get_avarage_scores(self):
        '''获取平均分'''
        # 方式一：
        # sum = self.en_score + self.math_score + self.cn_score
        # avg_score = sum / 3
        # 方式二：
        sum = self.get_all_scores()
        avg_score = sum / 3
        # print("平均分为：{}".format(self.get_all_scores() / 3))
        return avg_score


    def print_stu_info(self):
        '''打印学生信息'''
        print(f"我的名字叫{self.name}，年龄：{self.age}, 性别：{self.sex}。")

# # 学生1
# stu1 = Student("张三", 30, "男", 100, 130, 120)
# print(stu1.get_all_scores())
# print(stu1.get_avarage_scores())
# stu1.print_stu_info()
# # # 学生2
# stu2 = Student("lisa", 28, "女", 80, 130, 100)
# print(stu2.get_all_scores())
# print(stu2.get_avarage_scores())
# stu2.print_stu_info()

# 第四题 工具箱类和工具类
# 题目4:
# 编写一个工具箱类和工具类
# 工具类：需要有工具具的名称、功能描述、价格。
# 工具箱类：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
# 实例化几个工具。并在工具箱对象当中做添加/删除/查看工具操作，获取工具箱对象中有几个工具。
# 工具比如锤子、斧头、螺丝刀等工具。
# 提示：不需要用到继承。
'''工具箱类：
存放工具：[]
方法：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数（len()）

工具类：Tools
属性：名称、功能描述、价格 ---实例属性
方法：介绍工具信息 

实例化：
  工具实例化对象：  锤子、斧头、螺丝刀
'''

class Tool:
    def __init__(self,name,price,func_desc):
        self.name = name
        self.price = price
        self.func_desc = func_desc

    def print_tool_info(self):
        print(f"工具名称：{self.name}\t工具的价格: {self.price}\t工具的功能: {self.func_desc}\n")
# t1 = Tool()
# t2 = Tool()
# t1.print_tool_info()
# t1.name
# t1.price
# t1.func_desc

class ToolBox:
    def __init__(self):
        self.tools = []     # 工具类对象

    def add_tool(self,tool_obj:Tool): # Tool类的对象作为方法的参数
        '''添加工具'''
        self.tools.append(tool_obj)
        # if tool_obj not in self.tools:
        #     self.tools.append(tool_obj)
        # else:
        #     print("工具箱里已有！")

    def del_tool(self,tool_obj:Tool):
        '''删除工具'''
        if tool_obj in self.tools:
            self.tools.remove(tool_obj)
        else:
            print("工具箱里无此工具！")

    # 函数的参数  变量名: 数据类型/类    给形参一个注释 ，表示期望传入的类型。但是调用的时候可以传别的类型。
    def get_tool(self,tool_obj):
        if tool_obj in self.tools:
            tool_obj.print_tool_info()  # tool2.print_tool_info()
        else:
            print("工具箱里无此工具！")

    def get_count_of_tools(self):
        '''工具的数量'''
        count = len(self.tools)
        print("工具个数为：{}".format(count))

# # 实例化工具
tool1 = Tool("锤子",50, "刨根")
tool2 = Tool("螺丝刀",10, "拧螺丝")
tool3 = Tool("斧头",100, "砍树")
# # 实例化一个工具箱
tm = ToolBox()
# # # 添加一个工具
tm.add_tool(tool1)
tm.add_tool(tool2)
tm.add_tool(tool3)
tm.add_tool(tool1)
tm.get_count_of_tools()  # 查看工具箱里面有几个工具
tm.del_tool(tool1)
tm.get_count_of_tools()
tm.get_tool(tool1)  # 查看工具箱里tool2的介绍信息

