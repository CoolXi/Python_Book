# 对数值取整
import math


print(round(1234, -1))      # 输出: 1230（十位四舍五入）
print(round(1634.1, -3)) 
print(4.2+2.1)

from decimal import Decimal, localcontext, getcontext

print(0.1 + 0.2)    # 0.30000000000000004

a = Decimal('0.1')
b = Decimal('0.2')
c = Decimal('0.3')
print(a)            # 0.1
print(a + b)        # 0.3
print(a / c)        # 0.3333333333333333333333333333
print(getcontext().prec)    # 28，获取上下文精度，默认为 28

with localcontext() as ctx:
    ctx.prec = 3    # 修改上下文精度为 3 位小数
    print(a + b)    # 0.3
    print(a / c)    # 0.333


nums = [1.23e+18, -1.23e+18]
print(sum(nums))
print(math.fsum(nums))


a = 20
print(bin(a))  # 0b10100，十进制转二进制
print(oct(a))  # 0o24，十进制转八进制
print(hex(a))  # 0x14，十进制转十六进制

print(format(a, 'b'))  # 10100，省略前缀 0b
print(format(a, 'o'))  # 24，省略前缀 0o
print(format(a, 'x'))  # 14，省略前缀 0x


# 字节转整型
text =  b'\x01\x02'
print(int.from_bytes(text, 'big'))      # 输出 258,计算方式为 1 * 256 + 2 = 258
print(int.from_bytes(text, 'little'))   # 输出 513,计算方式为 2 * 256 + 1 = 513

num = 258
print(num.to_bytes(2, 'big'))           # 输出：b'\x01\x02'
print(num.to_bytes(2, "little"))        # 输出：b'\x02\x01'