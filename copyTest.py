import copy


# 测试浅拷贝和深拷贝
def testQianCopy():
    """浅拷贝"""
    a = [10, 20, [5, 6]]
    b = copy.copy(a)

    print(a)
    print(b)

    b.append(30)
    b[2].append(7)

    print(a)
    print(b)


def testDeepCopy():
    """深拷贝"""
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)

    print(a)
    print(b)

    b.append(30)
    b[2].append(7)

    print(a)
    print(b)


testDeepCopy()
print("-----")
testQianCopy()
