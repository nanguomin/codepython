from datetime import datetime
import arrow
from apscheduler.schedulers.blocking import BlockingScheduler


def job1():
    print("Hello job1")
    print(arrow.now().format('YYYY-MM-DD HH:mm:ss'))


def job2():
    print("Hello job2")
    print(arrow.now().format('YYYY-MM-DD HH:mm:ss'))


def job3():
    print("Hello job3")
    print(arrow.now().format('YYYY-MM-DD HH:mm:ss'))


def job4():
    print("Hello job4")
    print(arrow.now().format('YYYY-MM-DD HH:mm:ss'))


def job5():
    print("Hello job5")
    print(arrow.now().format('YYYY-MM-DD HH:mm:ss'))


def job_function():
    # BlockingScheduler
    sched = BlockingScheduler()
    # Schedule job_function to be called every two hours
    # sched.add_job(job_function, 'interval', hours=2)
    # The same as before, but starts on 2010-10-10 at 9:30 and stops on 2014-06-15 at 11:00
    t = arrow.now().format('YYYY-MM-DD')
    print(t)
    sched.add_job(job1, 'interval', minutes=2, start_date=t + ' 09:00:00', end_date=t + ' 10:15:00')
    sched.add_job(job2, 'interval', minutes=2, start_date=t + ' 10:30:00', end_date=t + ' 11:30:00')
    sched.add_job(job3, 'interval', minutes=2, start_date=t + ' 13:30:00', end_date=t + ' 16:00:00')
    sched.add_job(job4, 'interval', minutes=2, start_date=t + ' 09:30:00', end_date=t + ' 11:30:00')
    sched.add_job(job5, 'interval', minutes=2, start_date=t + ' 13:00:00', end_date=t + ' 15:00:00')
    # sched.add_job(job1, 'interval', seconds=5, start_date=t+' 19:00:00', end_date=t+' 19:30:00')
    # sched.add_job(job2, 'interval', seconds=10, start_date=t + ' 19:00:00', end_date=t + ' 19:15:00')
    start_date = t + ' 19:00:00'
    print(start_date)
    sched.start()
    sched.shutdown()


if __name__ == '__main__':
    job_function()
    list1 = [1, 2, 3, 4, 5]
    len(list1)