from datetime import datetime
import arrow
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time
def job1():
    t = arrow.now().format('YYYYMMDDHHmmss')
    a = ['1.python解释器', 'CPython', 'IPthon', 'PyPy', 'Jython', 'IronPython', '2.计算机编码', 'ASCLL', '不包含中文', '1个字节',
         'Unicode', '包含中文', '编码一般为2个字节', 'UTF-8', '包含中文,可变长编码', '英文1个字节,中文一般是3个字节', '计算机内存统一使用', 'Unicode编码', '3.数据结构',
         '元组', '列表', '字典', '4.条件判断', 'if', 'else', 'while', '5.循环', 'for', 'a', 'in', 'aa', '6.函数', '6.1', '定义函数',
         'def', 'myfunction()', 'return', '6.2', '函数参数', 'def', 'myfunction(a,b,c)', 'return', '可默认参数', '例:', 'def',
         'myfunction(a,b=1,c=2)', 'return', 'a+b+c', '调用', 'd=myfunction(1)', 'd=4', 'd=myfunction(1,3,4)', 'd=8',
         '可变参数(可以传入0或者任意个参数(参数在传递时会自动封装成一个tuple))', 'def', 'myfunction(*nums)', '调用', 'myfunction(1,2,3)', '可以传入不定个参数',
         'lists=[1,2,3]', 'myfunction(*lists)', '也可以传入list列表', '关键字参数(可以传入0和任意个参数,这些参数会被封装成dict)', 'def',
         'myfunction(**kw)', '命名关键字参数', 'def', 'myfunction(a,b,*,name,age)', '参数组合', 'python可以传入',
         '必选参数,默认参数,可变参数,命名关键字参数,关键字参数的组合参数', '但是参数的定义顺序必须是以上顺序', '高级特性', '1.列表表达式', '[x', '*', 'x', 'for', 'x', 'in',
         'range(1,', '11)]', '2.生成器', 'generator', 'g', '=', '(x', '*', 'x', 'for', 'x', 'in', 'range(10))', '3.迭代器',
         'Iterable', '可以用', 'isinstance()', '来判断一个对象是否是Iterable对象', '可以被next()函数调用并不断返回下一个值的对象称为迭代器', '高阶函数', 'map',
         'reduce', 'filter', 'sorted', '返回函数', '匿名函数', '装饰器', '偏函数', '面向对象', '1.类和实例', '定义类通过class关键字', '实例创建',
         ':类名+()', '2.私有属性', '在属性名前面加双下划线__', '3.继承多态', '4.获取对象信息', 'dir()', '获得一个对象的所有属性和方法']
    # print("Hello job1")
    # print(arrow.now().format('YYYY-MM-DD HH:mm:ss'))
    with open(t+'python.txt', 'w') as f:
        f.write(str(a))
        f.flush()
    print(a)
    print(t)


def job_function():
    # BlockingScheduler
    sched = BlockingScheduler()
    sched.add_job(job1, 'interval', seconds=10)
    sched.start()

if __name__ == '__main__':
    job_function()
