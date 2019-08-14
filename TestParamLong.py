# 可变参数
# 默认参数
# 指定参数名
# 可变参数后面加 参数 使用时 必须指定参数名
def f1(a, b, *c):
    print("c是元组")


def f2(a, b, **c):
    print("c是map")
