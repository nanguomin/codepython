import schedule
import time
import arrow
import threading
import os,sys
import arrow
from schedule import every, repeat
@repeat(every(5).seconds,"LTC")
def print01(name):
    print("hello ",name)
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == '__main__':
  print01("LTC")