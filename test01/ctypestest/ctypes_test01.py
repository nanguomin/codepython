import platform
from ctypes import *


def test01():
    if platform.system() == 'Windows':
        libc = cdll.LoadLibrary('msvcrt.dll')
        return libc
    elif platform.system() == 'Linux':
        libc = cdll.LoadLibrary('libc.so.6')
        return libc


# libc.printf('%s\n', 'here!')  # here!
# libc.printf('%S\n', u'there!')  # there!
# libc.printf('%d\n', 42)  # 42
# libc.printf('%ld\n', 60000000)  # 60000000
#
# # libc.printf('%f\n', 3.14)          #>>> ctypes.ArgumentError
# # libc.printf('%f\n', c_float(3.14)) #>>> dont know why 0.000000
# libc.printf('%f\n', c_double(3.14))  # 3.140000
class Bottles(object):
    def __init__(self, number):
        self._as_parameter_ = number  # here only accept integer, string, unicode string


if __name__ == '__main__':
    test01 = test01()
    print(type(test01), test01)
    print('==Hello ctypes==:', test01.printf('Hello ctypes!\n'))
    print('==here==:', test01.printf('%s\n', 'here!'))
    print('==u_there!==:', test01.printf('%S\n', u'there!'))
    print('==42==:', test01.printf('%d\n', 42))
    print('==60000000==:', test01.printf('%ld\n', 60000000))
    bottles = Bottles(42)
    print('==bottles==:', test01.printf('%d bottles of beer\n', bottles))
