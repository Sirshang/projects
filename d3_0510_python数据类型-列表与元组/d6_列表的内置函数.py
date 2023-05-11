'''
- 3、列表内置函数
  - 列表中的元素求和,sum(列表名)
  - 列表中元素的排序：
    - 列表名.sort()   ---升序排列，从小到大排序
    - 列表名.sort(reverse = True)  ---降序排列，从大到小排序
  - 倒序输出：列表名.reverse()
  - 获取元素的索引值：index(元素)

'''

num = [10,2,31,14,5,26,57]
# res = sum(num)
# print(res)

num.sort()
print(num)

# num.reverse()
# print(num)

# num.sort(reverse = True)
# print(num)

print(num.index(14))
# print(num.index('abc'))  # 元素不存在，则会报错



