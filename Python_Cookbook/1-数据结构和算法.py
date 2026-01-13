from os import name
from typing import Any


from loguru import logger


# 解包
a, b, [c, d] = ["hello", 2, ('a', 'b')]
logger.debug(a, b, c, d)

*a, b = [10, 8, 7, 1, 9, 5, 10, 5] 
logger.debug(a)    # [10, 8, 7, 1, 9, 5, 10]
logger.debug(sum(a) / len(a))


# 固定长度的序列 collections.deque
from collections import defaultdict, deque

my_deque = deque(maxlen=3)
my_deque.append(1)
my_deque.appendleft(2)
my_deque.append(3)
logger.debug(my_deque)  # deque([2, 1, 3], maxlen=3)
my_deque.append(4)
logger.debug(my_deque)  # deque([1, 3, 4], maxlen=3)
my_deque.popleft()
logger.debug(my_deque)  # deque([3, 4], maxlen=3)


# 优先级队列
import heapq
# 获取序列中前 N 个最大或最小的元素
my_list = [4, 1, 5, 5, 2, 8, -1, 6, 9]
logger.debug(f'前 2 个最大值：{heapq.nlargest(2, my_list)}')    # [9. 8]
logger.debug(f'前 2 个最小值：{heapq.nsmallest(2, my_list)}')   # [-1, 1]
# 创建堆结构
logger.debug(my_list)   # [4, 1, 5, 5, 2, 8, -1, 6, 9]
heapq.heapify(my_list)
logger.debug(my_list)   # [-1, 1, 4, 5, 2, 8, 5, 6, 9]

p = heapq.heappop(my_list)
logger.debug(p)     # -1
logger.debug(my_list)   # [1, 2, 4, 5, 9, 8, 5, 6]
p = heapq.heappush(my_list, 101)
logger.debug(p)     # None
logger.debug(my_list)   # [1, 2, 4, 5, 9, 8, 5, 6, 101]


# 默认字段 defaultdict
pairs = ["a", "b", "a"]
my_defaultdict = defaultdict[Any, list](list)
for i in pairs:
    my_defaultdict[i] = 1
logger.debug(my_defaultdict)

from collections import OrderedDict

d1 = OrderedDict([('a', 1), ('b', 2)])
d2 = OrderedDict([('b', 2), ('a', 1)])
logger.debug(d1 == d2)  # False，顺序不同

d3 = {'a': 1, 'b': 2}
d4 = {'b': 2, 'a': 1}
logger.debug(d3 == d4)  # True

#去重且保持顺序
my_list = [2,5,5,3,7,4,4,2,9,1,5]
my_d = OrderedDict()
logger.debug(my_d)
for i in my_list:
    my_d[i] = 0
logger.debug(my_d)
logger.debug(list(my_d))


# zip() 组合
my_dict = {'zhangsan': 18, 'lisi': 25, "wangwu": 17, "zhaoliu": 22}
print(f'最大值：{max(zip(my_dict.values(), my_dict.keys()))}')  # 最大值：(25, 'lisi')
print(f'最小值：{min(zip(my_dict.values(), my_dict.keys()))}')  # 最小值：(17, 'wangwu')
print(f"排序：{sorted(zip(my_dict.values(), my_dict.keys()))}") # 排序：[(17, 'wangwu'), (18, 'zhangsan'), (22, 'zhaoliu'), (25, 'lisi')]


def dedupe(items):
    my_set = set()
    for item in items:
        if item not in my_set:
            my_set.add(item)
            yield item

a = [2,5,5,3,7,4,4,2,9,1,5]
logger.debug(list(dedupe(a)))
logger.debug(dedupe(a))


# 切片
a = "hello 666 world"
sli = slice(6, 9)
print(a[sli])   # 666

s_in = sli.indices(len(a))
print(s_in)     # (6, 9, 1)
for i in range(*s_in):
    print(a[i])

print(slice(-2, None, 10).indices(5))


# 计数
from collections import Counter

a = Counter(['a', 'b', 'c', 'a'])
b = Counter(['a', 'b', 'd'])
print(a)   # Counter({'a': 2, 'b': 1, 'c': 1})
print(b)   # Counter({'a': 1, 'b': 1, 'd': 1})

print(a + b)    # Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
print(a - b)    # Counter({'a': 1, 'c': 1})


# 排序
from operator import itemgetter

func = itemgetter(1)
print(func("abc"))  # b，调用 func 函数，获取返回值，相当于 "abc"[1]，因此得到 "b"

name_info = [
    ("zhangsan", 18),
    ("lisi", 25),
    ("wangwu", 20)
]

new_list = sorted(name_info, key=itemgetter(1))
print(new_list)     # [('zhangsan', 18), ('wangwu', 20), ('lisi', 25)]


# 分组
from itertools import groupby

rows = [ 
    {'address': '5412 N CLARK', 'date': '07/01/2012'}, 
    {'address': '5148 N CLARK', 'date': '07/04/2012'}, 
    {'address': '5800 E 58TH', 'date': '07/02/2012'}, 
    {'address': '2122 N CLARK', 'date': '07/03/2012'}, 
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, 
    {'address': '1060 W ADDISON', 'date': '07/02/2012'}, 
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'}, 
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, 
] 

new_rows = sorted(rows, key=itemgetter("date")) # 先排序
print(new_rows) 

for key, value in groupby(new_rows, key=itemgetter("date")):
    print(key, list(value))


# 筛选
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
new_list = [n for n in mylist if n > 0]
print(new_list)

new_list_1 = []
for i in mylist:
    if i < 0:
        new_list_1.append(0)
    else:
        new_list_1.append(i)
print(new_list_1)

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
new_list = [n if n >= 0 else 0 for n in mylist]
print(new_list) # [1, 4, 0, 10, 0, 2, 3, 0]

portfolio = [ 
   {'name':'GOOG', 'shares': 50}, 
   {'name':'YHOO', 'shares': 75}, 
   {'name':'AOL', 'shares': 20}, 
   {'name':'SCOX', 'shares': 65} 
] 

# 获取最小的 shares 值
min_shares = min(x["shares"] for x in portfolio)
print(min_shares)   # 20

# 获取最小的 shares 所在的元素
min_item = min(portfolio, key=lambda x: x["shares"])
print(min_item)     # {'name':'AOL', 'shares': 20}

my_list = [{'name': 'zhangsan', 'age': 30}, 
           {'name': 'lisi','age': 18}, 
           {'name': 'wangwu', 'age': 18},
           {'name': 'zhaoliu', 'age': 30}]
print(max(my_list, key=lambda x: x['age']))  # {'name': 'zhangsan', 'age': 30}，返回第一个最大值
print(min(my_list, key=lambda x: x['age']))  # {'name': 'lisi', 'age': 18}，返回第一个最小值
print(min(x["age"] for x in my_list))        # 18，返回最小的 age 值