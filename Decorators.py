__author__ = 'shuxieliu'

import sys

debug_log = None #sys.stdout

def trace(func):
    if debug_log != None:
        def callf(*arg,**kwargs):
            debug_log.write('call function {0} \n'.format(func.__name__))
            ret = func(*arg,**kwargs)
            debug_log.write('function return {0}\n.'.format(ret))
        return callf
    else:
        return func

@trace
def square(x):
    return x*x+1


print square(4)
print square.__globals__
print square.__name__
print square.__doc__

print('sys' in square.__globals__)