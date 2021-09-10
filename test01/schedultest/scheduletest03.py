import schedule
import time
import arrow
import threading
import os,sys
import arrow

def job1():
    # t1=arrow.now().format('YYYYMMDDHHmmss')
    # path=sys.path[0]
    # path=path+'/'+t1
    # os.mkdir(path)
    # print(type(path),path)
    print("Hello job1")

def job2():
    print("Hello job2")
def run_thead(thead_func):

    thead1=threading.Thread(target=thead_func)
    thead1.start()


def scheduletest01():
    t1 = arrow.now().format('HH:mm:ss')
    t2='15:00:00'
    t3='16:00:00'
    if t1<t2:
        schedule.every().second.do(job1)
        print("当前时间早于下午4点")
    if t1>t3:
        schedule.every().second.do(job2)
        print("当前时间晚于下午4点")
    print(t1)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == '__main__':

    schedule.every(5).seconds.do(scheduletest01)
    while True:
        schedule.run_pending()
        time.sleep(1)

