# 编写一个函数，接受 str 或 bytes，并返回 str
def get_str(arg) -> str:
    if isinstance(arg, bytes):
        arg = arg.decode("utf-8")
    return arg

print(get_str("hello"))

# 编写一个函数，接受 str 或 bytes，并返回 bytes
def get_bytes(arg) -> bytes:
    if isinstance(arg, str):
        arg = arg.encode("utf-8")
    return arg

print(get_bytes('你好'))
print(get_bytes(b'12ab'))


