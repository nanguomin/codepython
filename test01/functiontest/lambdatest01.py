def lambda_test01():
    # 单个参数
    g = lambda x: x ** 2
    print(g(3))
    # 多个参数
    l = lambda x, y, z: (x + y) * z
    print(l(1, 2, 2))


def lambda_test02():
    print(list(map(lambda x: x * x, [y for y in range(10)])))
    f = lambda x: x + 1
    a = [1, 2, 3]
    print(list(map(f, a)))


if __name__ == '__main__':
    lambda_test01()
    lambda_test02()
