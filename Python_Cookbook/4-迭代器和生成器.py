x = [1, 2, 3]

def div_iter():
    i = iter(x)
    while True:
        res = next(i, None)
        print(res)
        if res == None:
            return

div_iter()


# 委托迭代：将自定义的对象委托给内部对象进行迭代操作

class Node:
    def __init__(self, node) -> None:
        self._node = node
        self._children = []
    
    def __repr__(self) -> str:
        return f"Node({self._node!r})"
    
    def __iter__(self):
        # 将当前对象 Node 的迭代请求委托给对象内部的 self._children 上（即委托给列表对象）
        return iter(self._children)
    
    def add_children(self, node):
        self._children.append(node)
    

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_children(child1)
root.add_children(child2)
print(root._children)       # [Node(1), Node(2)]

for i in root:              # 遍历 root 即调用 __iter__，内部遍历的是 self._children 列表
    print(i)                # Node(1)、Node(2)


# 用生成器实现自定义 range 函数
def frange(start, stop, step):
    while start < stop:
        yield start
        start += step

x = frange(0, 1, 0.2)   # 生成器器
print(x)                # <generator object frange at 0x00000166A450B1D0>
for i in x:
    print(i)            # 0、0.2、0.4、0.6000000000000001、0.8


#  定义一个反向迭代
class CountDown:
    def __init__(self, value) -> None:
        self.value = value
    
    def __iter__(self):
        n = 0
        while n < self.value:
            yield n
            n += 1
    
    def __reversed__(self):
        n = self.value - 1
        while n >= 0:
            yield n
            n -= 1
            

x = CountDown(5)
for i in x:
    print(i)

for i in reversed(x):
    print(i)


import time

# # 装饰函数
# def demo(fn):  # 接收一个参数 fn，fn 即为被装饰的函数
#     def inner(*args, **kwargs):
#         time1 = time.time()
#         fn(*args, **kwargs)  # 相当于执行了被装饰函数
#         time2 = time.time()
#         return time2 - time1
#     return inner

# # 被装饰的函数
# @demo  # 当执行到该行代码时,相当于执行了 test=demo(test)
# def test():
#     time.sleep(1)
#     print('该 test 函数被执行了')

# test()  # 调用 test 函数

a = ['1', '2', '3']
b = ('k', 'm', 'n', 'l')
print(list(zip(a, b)))
for i, j in zip(a, b):
    print(i, j)