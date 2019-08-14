# 测试eval()函数
# 执行一段代码
eval("print('asd')")

a = 10
b = 20
c = eval("a+b")
print(c)

dict1 = dict(a=100, b=200)
# 使用了dict1中的参数
d = eval("a+b", dict1)
print(d)
print(a, b)
