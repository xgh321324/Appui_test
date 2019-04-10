# coding:utf-8


class A(object):
    def __init__(self):
        self.namea = "aaa"

    def funca(self):
        print ("function a : %s"%self.namea)

class B(A):
    def __init__(self):
        #这一行解决问题
        super(B,self).__init__()
        self.nameb="bbb"

    def funcb(self):
        print ("function b : %s"%self.nameb)

b=B()
print (b.nameb)
b.funcb()
b.funca()
