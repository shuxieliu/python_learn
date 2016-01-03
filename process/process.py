#coding=utf-8
__author__ = 'shuxieliu'

import multiprocessing
import os,time



class cls(object):
    def __init__(self, a):
        print 'test init.'
        self.a = 11
    def Add(self, b):
        print 'cls function Add called begin.'
        print self.a + b
        print 'cls function Add called end.'

def funcA(aa):
    print 'sub_process begin.'
    print 'funcA is called. value is {}'.format(aa)
    print 'sub_process end.'

def lock_time(name):
    print 'Run task {}({}): start !'.format(name, os.getpid())
    start = time.time()
    time.sleep(1)
    end = time.time()
    print 'Run task {}({}) end, consume time is {}!'.format(name, os.getpid(), end - start)

def  QueWrite(queue):
     for value in {'mike': 20, 'jack':40, 'lucy': [10,20,30]}:
         print 'put elem {} into queue.'.format(value)
         queue.put(value)
         time.sleep(1)

def QueRead(queue):
    while True:
        if not queue.empty():
            value = queue.get()
            print 'get elem {} from queue.'.format(value)
            time.sleep(1)
        else:
            break

def process_test():
    p = multiprocessing.Process(target=funcA, args=(10,))
    p.start()
    p.join()

    print 'porcess_test end.'

def process_pool_test():
    pool = multiprocessing.Pool()
    for i in range(5):
        pool.apply_async(func=lock_time, args=(i,))

    '''在join之前一定要先close'''
    pool.close()
    pool.join()

    print 'process_pool_test end.'

def Queue_test():
    queue = multiprocessing.Queue()
    proc_w = multiprocessing.Process(target=QueWrite, args=(queue,))
    proc_r = multiprocessing.Process(target=QueRead, args=(queue,))

    proc_w.start()
    proc_r.start()
    proc_w.join()
    proc_r.join()

    print 'Queue_test end.'

if __name__ == '__main__':
    process_test()
    process_pool_test()
    Queue_test()





