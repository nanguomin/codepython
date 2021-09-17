import ctypes
import platform
from ctypes import *


if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() == 'Linux':
    libc = cdll.LoadLibrary('libc.so.6')


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
    bottles = Bottles(42)
    print(libc.printf('%d bottles of beer\n', bottles))
    print(ctypes.CDLL('msvcrt.dll'))
