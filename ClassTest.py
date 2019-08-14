class Stu:

    # def __new__(cls, *args, **kwargs):
    #     print("创建对象")

    # 构造函数 self 指自己
    def __init__(self, name, score):
        self.name = name
        self.__score = score  # 私有属性 实际仍然可以操作 变成 _Stu__score

    def __work(self):  # 私有方法 实际变成 _Stu__work
        print("好好工作")


def say_score(self):
    print("{0} 分数是{1}".format(self.name, self.score))


s1 = Stu("name1", 98)
s1.say_score()

print(dir(s1))
print(s1.__dict__)


# 空的类
class Man:
    pass


# isinstance 判断对象的类型
print(isinstance(s1, Stu))
print(isinstance(s1, Man))
