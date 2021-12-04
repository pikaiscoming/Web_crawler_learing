# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:15:53 2021

@author: pikachu
"""

'''
review the 'class'
'''

import threading, time

class Crawler(threading.Thread): #繼承
    def __init__(self):
        threading.Thread.__init__(self)
        self.done = False
        
    def isDone(self):
        return self.done
    
    def run(self):
        time.sleep(5)
        self.done = True
        raise Exception('Something bad happened!')
        
t = Crawler()
t.start()
while True:
    time.sleep(1)
    if t.isDone():
        print('Done')
        break
    if not t.isAlive():
        t = Crawler()
        t.start()
        
''' can use Crawler.run to let exceptions restart.'''

from multiprocessing import Process

def printtime(threadname, delay, iterations):
    start = int(time.time())
    for i in range(0, iterations):
        time.sleep(delay)
        timeinterval = str(int(time.time()-start))
        print("{} {}".format(timeinterval, threadname))
        e = time.time()-start
        if e>=10:
            break

processes = []
processes.append(Process(target=printtime, args=('Counter', 1, 100)))
processes.append(Process(target=printtime, args=('Fizz', 3,33)))
processes.append(Process(target=printtime, args=('Buzz', 5, 20)))

for p in processes:
    p.start()
    
for p in processes:
    p.join()  #"wait for this [thread/process] to complete

        
