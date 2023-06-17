import pymysql
from pymysql.cursors import DictCursor

'''- 操作数据库步骤：
  - 1、创建连接
  - 2、获取游标
  - 3、进行sql操作，提取数据（一般结合查询sql来使用）
    cursor.fetchone()
    cursor.fetchall()
  - 4、关闭游标
  - 5、关闭连接
'''
# 1、创建连接
connect = pymysql.connect(user='lemon',
                            password="lemon123",
                            host='47.113.180.81',
                            database='yami_shops',
                            port=3306)
# 2、获取游标
cursor = connect.cursor(cursor = DictCursor)
select_sql = "select user_phone,mobile_code from tz_sms_log where user_phone = '13211112222' order by rec_date desc limit 1;"
# 3、进行sql操作
res = cursor.execute(query = select_sql)
# print(res) # 这里获取的是查询结果的记录数
# 通过游标提取数据
# data1 = cursor.fetchone()
# print(data1)
# data2 = cursor.fetchone()
# print(data2)

data_all = cursor.fetchall()
print(data_all)  # (('13211112222', '493217'),)

#在创建游标的时候加上参数：cursor = DictCursor，可以将数据转为列表嵌套字典格式 [{'user_phone': '13211112222', 'mobile_code': '493217'}]
code = data_all[0]['mobile_code']
print(code)

# 4、关闭游标
cursor.close()
# 5、关闭连接
connect.close()


# 封装？
