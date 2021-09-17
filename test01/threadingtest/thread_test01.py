import threading
import time

event = threading.Event()


def test01(name):
    event.clear()
    print('%s 启动成功' % threading.currentThread().getName())
    print('%s 正在测试线程!!!' % name)
    # time.sleep(1)
    # event.wait()
    print('%s 启动成功' % threading.currentThread().getName())
    print('%s 测试成功!!!' % name)


threads = []
threading1 = threading.Thread(target=test01, args=("a",))
threading2 = threading.Thread(target=test01, args=("b",))
threads.append(threading1)
threads.append(threading2)

for thread in threads:
    thread.start()

time.sleep(0.1)
