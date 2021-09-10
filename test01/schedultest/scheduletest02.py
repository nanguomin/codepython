import schedule
import time
import arrow
import threading

def job1():
    print("I'm working ..... in job1 start ")
    time.sleep(5)
    print("I'm working ..... in job1 end ")

def job2():
    print("I'm working ..... in job2 start ")
    # time.sleep(5)
    print("I'm working ..... in job2 end ")
def scheduletest01():

    #每隔5秒执行一次任务
    schedule.every(5).seconds.do(job1)
    schedule.every(5).seconds.do(job2)
    #每隔1小时执行一次
    # schedule.every().hour.do(job)
    #每天的10:30执行
    # schedule.every().day.at("10:30").do(job)
    #每隔5到10天执行一次
    # schedule.every(5).to(10).days.do(job)
    #每天周一的时候执行
    # schedule.every().monday.do(job)
    # 每天周三13:15执行
    # schedule.every().wednesday.at("13:15").do(job)


    while True:
        schedule.run_pending()
        time.sleep(1)

def run_thread(job_func):
    job_thread=threading.Thread(target=job_func)
    job_thread.start()

def scheduletest02():
    schedule.every(5).seconds.do(run_thread,job1)
    schedule.every(5).seconds.do(run_thread,job2)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    #单线程
    # scheduletest01()
    #多线程
    scheduletest02()