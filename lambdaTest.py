# lambda表达式 匿名函数
# 定义简单的函数
f = lambda a, b, *c: a + b + c[1]
print(f(1, 2, 3, 2))

g = [lambda a: a * 2, lambda b: b * 3, lambda c: c * 4]
print(g[0](2))
