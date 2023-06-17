''''''
'''- 读取Excel文件中数据的步骤：
  - 1、打开excel文件
  - 2、获取sheet
  - 3、读取操作
  - 4、写入操作，一定要记得保存文件
'''
import openpyxl
# excel的函数封装：快去的去读取任意的.xlsx下的任意sheet中的数据
def read_excel(file_name,sheet_name):
    '''
    读取excel中某个sheet所有的数据
    :param file_name: excel文件的路径和名称，格式.xlsx
    :param sheet_name: excel文件中sheet的名称
    :return: 所有的数据，列表嵌套字典的格式
    '''
    book = openpyxl.load_workbook(filename=file_name)
    sh1 = book[sheet_name]
    all_data = list(sh1.values)
    new_all_data = []
    title = all_data[0]
    for case in all_data[1:]:
        new_case = dict(zip(title, case))
        new_all_data.append(new_case)
    return new_all_data

