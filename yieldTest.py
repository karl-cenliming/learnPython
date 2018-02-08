__author__ = 'liming'
# example from following url
# https://www.jianshu.com/p/d09778f4e055
def g():
    print '1'
    x = yield 'hello'
    print '2', 'x=', x
    y = 5 + (yield x)
    print '3', 'y=', y

# f = g()
#f.next()
#f.send(5)
#f.send(2)

