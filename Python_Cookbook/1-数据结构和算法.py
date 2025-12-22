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
            yield item
            my_set.add(item)

a = [2,5,5,3,7,4,4,2,9,1,5]
logger.debug(list(dedupe(a)))
logger.debug(dedupe(a))