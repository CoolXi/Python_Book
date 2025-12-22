"""
列表推导：根据某个序列或可迭代对象派生出一份新的列表
map：用于给序列或可迭代对象的每一项执行某个相同的操作
filter：对序列或可迭代对象进行过滤

与列表推导相似的还有字典推导和集合推导，用法几乎一致
"""

# 示例1：将列表中每个元素的平方值构建一份新的列表
# 方法1-使用 for 循环的写法如下：
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for i in numbers:
    squares.append(i ** 2)
print(squares)              # 输出：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 方法2-使用内置函数 map() 实现如下：
squares_map = map(lambda x: x ** 2, numbers)
print(list(squares_map))    # 输出：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

# 方法3-使用列表推导方式实现如下：
squares_list = [x**2 for x in numbers]
print(squares_list)         # 输出：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 示例2：将列表中的偶数的平方值构建一份新的列表
# 方法1-使用内置函数 map() 和 filter() 组合实现
squares_map = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
print(list(squares_map))    # 输出：[4, 16, 36, 64, 100]

# 方法2-使用列表推导方式实现如下：
squares_list = [x**2 for x in numbers if x % 2 == 0]
print(squares_list)         # 输出：[4, 16, 36, 64, 100]

# 总结，以上的两个示例中，使用列表推导的方式不仅语法简洁，且更容易让读者理解