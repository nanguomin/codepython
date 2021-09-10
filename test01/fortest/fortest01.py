def test(num):
    return num *2


if __name__ == '__main__':
    c = [[7, 8, 9], [1, 2, 3], [4, 5, 6]]
    l = []
    d = [test(b[0]) for b in c]
    for b in c:
        for a in b:
            l.append(a)
    print(l)
    print(d)
