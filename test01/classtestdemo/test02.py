import logging
from classtestdemo import sudent

logging.basicConfig(level=logging.ERROR)


def array01():
    aa = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    logging.info(aa)
    return aa


if __name__ == '__main__':
    # list1, list2, list3 = [], [], []
    # for a in array01():
    #     if -2 <= a < 0:
    #         list1.append(a)
    #     elif a < -2:
    #         list2.append(a)
    #     else:
    #         list3.append(a)
    # print("大于-2小于0:", list1)
    # print("小于-2:", list2)
    # print("大于0:", list3)

    # try:
    #     a = 0
    #     b = 10
    #     c = b / a
    # except ZeroDivisionError as e:
    #     logging.info(e)
    student = sudent.Student('小明', '18', '男')
    print(student.print01())
    print("test")
