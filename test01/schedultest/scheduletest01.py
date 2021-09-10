import schedule
import time
import arrow

def job():
    print("I'm working....")
def scheduletest():

    #每隔5秒执行一次任务
    schedule.every(5).seconds.do(job)
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
if __name__ == '__main__':
    scheduletest()