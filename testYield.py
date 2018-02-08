# encoding:UTF-8
__author__ = 'liming'


def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
    #做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    return i * 2

#使用for循环
for i in yield_test(5):
    print("point 1: {}".format(i))

#作者：千若逸
#链接：https://www.jianshu.com/p/d09778f4e055
#來源：简书
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
