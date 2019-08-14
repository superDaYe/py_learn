# 嵌套函数
# 内部的函数 只能在内部使用
# 在封装的时候可以使用
def outer():
    print("outer!!")

    def inner():
        print("inner!")

    inner()

outer()
