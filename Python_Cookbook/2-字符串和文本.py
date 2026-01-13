# 创建转换表，将 s 转成 c
table1 = str.maketrans('s', 'c')
show = "this is a apple"
print(show.translate(table1))  # thic ic a apple

# 创建转换表，将 s 转成 c，将 a 转成 k，去掉空格
table2 = str.maketrans('sa', 'ck', ' ')
show = "this is a apple"
print(show.translate(table2))  # thicickkpple

table3 = {
    ord("\t"): " ",
    ord("\f"): " ",
    ord("i"): "a"
}
show = "this\fis\tbook."
print(show.translate(table3))



text = "hello"
print(text.ljust(10, "*"))

x = 1.2345
print(format(x, "+^10.2f"))

data = ['ACME', 50, 91.1] 
print(" ".join(str(x) for x in data))

def sample(): 
    yield 'Is' 
    yield 'Chicago' 
    yield 'Not' 
    yield 'Chicago?' 

print(" ".join(sample()))


class myClass1(dict):
    def __missing__(self, key):
        value = "hello"
        return value

c = myClass1()
print(c['a'])


import textwrap
text = "Python是一种广泛使用的高级编程语言，以其简洁易读的语法而闻名。"
wrapped_text = textwrap.wrap(text, width=10, initial_indent="*", subsequent_indent="#")
print(wrapped_text)
# 输出: ['*Python是一种', '#广泛使用的高级编程', '#语言，以其简洁易读', '#的语法而闻名。']

wrapped_text_1 = textwrap.fill(text, width=10, initial_indent="*", subsequent_indent="#")
print(wrapped_text_1)
# 输出如下：
# *Python是一种
# #广泛使用的高级编程
# #语言，以其简洁易读
# #的语法而闻名。

print(b'%10s %10d %10.2f' % (b'ACME', 100, 490.1) )
print( b'{} {} {}'.format(b'ACME', 100, 490.1))