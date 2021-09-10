import os
def job(*numbers): #可变参数
    print(type(numbers),numbers)

    for number in numbers:
        print(number)

def job1(**numbers): #关键字参数
    print(type(numbers),numbers)

    for k,v in numbers.items():
        print(k,v)


if __name__ == '__main__':
    # list01 = [1, 2, 3, 4, 5, 6]
    # list=list(map(str,list01))
    # print(sum(list01))
    # print(list)
    # job(1,2,3,5)
    # job1(nane='ngm',age=18)
    a = os.name
    print(a)

