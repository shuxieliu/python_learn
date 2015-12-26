__author__ = 'shuxieliu'
import psutil
import datetime
from IPy import IP

import  functools

print 'hello world'

cpuTime = psutil.cpu_times()
cpuCount = psutil.cpu_count()
mem  = psutil.virtual_memory()
print cpuTime.user,cpuCount,mem.total,mem.available

"""pids = psutil.pids()
for pid in pids:
    p = psutil.Process(pid)
    #print p.name(),p.exe(),p.cwd(),p.status()
    print p.memory_info()
    conn = p.connections()
    if conn != []:
        print conn

ipseg = IP('192.168.4.0/22')
print ipseg.len()
for i in ipseg:
    print i
"""
def add(a,b):
    return a + b

add3 = functools.partial(add, 3)
add4 = functools.partial(add, 4)

print add3(1)

