import arrow

a = {'a': 1, 'b': 2, 'c': 3}

beginTime = arrow.now().format('YYYY-MM-DD HH:mm:ss')
if __name__ == '__main__':
    b = a.get('a', '-$')
    print(b)
    print('beginTime:{}'.format(beginTime))
    pass
