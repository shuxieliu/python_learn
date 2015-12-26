__author__ = 'shuxieliu'


class FooParent(object):
    def __init__(self):
        self.parent = 'this is parent.'
        print 'parent init func called.'

    def bar(self, msg):
        print '{0},{1}'.format(msg,'from parent')

class FooChild(FooParent):
    def __init__(self):
        super(FooChild,self).__init__()
        print 'child init finished.'

    def bar(self, msg):
        super(FooChild, self).bar(msg)
        print 'child bar called'
        print 'parent:{}'.format(self.parent)

