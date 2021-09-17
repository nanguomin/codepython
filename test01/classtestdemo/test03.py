import re
import ctypes


class dir_test():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_value(self):
        p = re.compile("__.*__")
        result = ""
        for value in dir(self):
            if p.search(value) == None and value != 'get_value':
                a = str(value) + "=" + str(getattr(self, str(value))) + ";"
                result += a
        return result.strip(";")


class str_test(ctypes.Structure):
    _fields = [('xiaomin', ctypes.c_char_p), ('hua', ctypes.c_char_p), ('uzi', ctypes.c_char_p)]

    def __str__(self):
        return innerStr(self)


def innerStr(cls):
    s = ""
    for value in cls._fields:
        if value[0] in ['xiaomin']:
            value = getattr(cls, value[0])
        elif value[0] == '':
            a = ''
        else:
            if isinstance(getattr(cls, value[0]), bytes):
                a = getattr(cls, value[0])
            else:
                a = getattr(cls, value[0])
        s += value[0] + ":" + str(value) + ","
    return s


if __name__ == '__main__':
    dir_test = dir_test('xiaoming', '17', '0')
    dir_test_value = dir_test.get_value()
    print('')
    print(type(dir_test_value), dir_test_value)
