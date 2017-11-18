class A(object):
    def __init__(self):
        print("in here")
    def cat(self,name):
        print("my cat",name)

A.cat(A(),"Tom")
