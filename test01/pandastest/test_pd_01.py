import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

# 参考菜鸟教程学习


def pandas_test_01():
    my_dataset = {
        'sites': ["Google", "Runoob", "Wiki"],
        'number': [1, 2, 3]
    }
    data_frame = pd.DataFrame(my_dataset)
    print(data_frame)


"""
Pandas 数据结构 - Series
"""


def pandas_test_02():
    a = [1, 2, 3]
    pd_series = pd.Series(a)
    print(pd_series)
    # 指定索引
    b = ["Google", "Runoob", "Wiki"]
    my_var = pd.Series(b, index=["x", "y", "z"])
    print(my_var)
    # key/value 创建pandas对象
    sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
    my_sites = pd.Series(sites)
    print(my_sites)


"""
Pandas 数据结构 - DataFrame
"""


def pandas_test_03():
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
    pd_data = pd.DataFrame(data)
    print(pd_data)
    # 返回第一行
    print(pd_data.loc[0])
    # 返回第二行
    print(pd_data.loc[1])
    # 返回第一行和第二行
    print(pd_data.loc[[0, 1]])


"""
Pandas CSV 文件
read_csv 读取csv文件
to_csv 保存成csv文件
head(n) 读取前n行 若无参数n 默认返回前5行
tail(n) 读取尾部的n行 无参数n 默认返回5行
info()  返回表格的基本信息
"""


def pandas_test_04():
    pd_read_csv = pd.read_csv('nba.csv')
    # print(pd_read_csv.to_string())
    print(pd_read_csv)
    name = ['mm', 'dd', 'cc', 'aa', 'bb']
    age = [12, 13, 14, 15, 16]
    gender = ['男', '女', '男', '女', '女']
    person_dict = {'name': name, 'age': age, 'gender': gender}
    pd_to_csv = pd.DataFrame(person_dict)
    pd_to_csv.to_csv('person.csv')


"""
Pandas JSON
"""


def pandas_test_05():
    pd_read_json=pd.read_json('sites.json')
    print(pd_read_json.to_string)


if __name__ == '__main__':
    # pd_version = pd.__version__
    # logging.info(pd_version)
    # pandas_test_01()
    # pandas_test_02()
    # pandas_test_03()
    # pandas_test_04()
    pandas_test_05()
