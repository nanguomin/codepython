"""
n维数组对象 Ndarray

ndarray 有以下组成部分
1.一个指向数据的指针
2.数据类型或dtype,描述在数组中的固定大小值的格子
3.一个表示数组形状(shape)的元组,表示各维度大小的元组
4.一个跨度元组(stride),其中的整数指的是为了前进到当前维度下一个元素需要'跨越'的字节数
"""


def enum(**enums):
    return type('Enum', (), enums)


TradeType = enum(LIMIT="0", Q="Q", R="R")

if __name__ == '__main__':
    print(enum())
    pass
