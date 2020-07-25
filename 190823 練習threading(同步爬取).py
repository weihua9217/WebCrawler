import threading
import time
from amazon_top_100 import select


class MyThread(threading.Thread):
    def __init__(self, num, code):
        threading.Thread.__init__(self)
        self.num = num
        self.code = '000'+ str(code)

    def run(self):
        print(select(self.num, self.code))
        select(self.num, self.code).to_csv('./top100/'+self.code+'.csv')


target = [2, 4, 6, 7, 8]
# 11, 12, 13, 15, 17, 20, 22, 23, 24, 26, 29, 30, 31, 32, 36, 38, 39]
threads = []
for i in range(0, 5):
    threads.append(MyThread(target[i], target[i]))
    threads[i].start()

for i in range(5):
    threads[i].join()

print('Done')

# threading.Thread(target=print(select(2, '0002'))).start()
# print(select(4, '0004'))
# threading.Thread(target=print(select(2, '0002'))).join()
# print('Done')

