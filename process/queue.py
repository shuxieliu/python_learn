__author__ = 'shuxieliu'

import Queue

q = Queue.Queue(10)

q.put('shu')
q.put(4)
q.put(['sxl', 30])

while q.qsize():
    print q.get()


