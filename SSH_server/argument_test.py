# import sys
#
# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', sys.argv[0])

# from subprocess import Popen, PIPE
# print('---')
# p = Popen(["ls", "-la"], stdout=PIPE)
# out, err = p.communicate()
# print(out.decode("UTF-8"))
# print('---')
# a = 'hello'.encode('UTF-8')
# print('--')
# import queue
# item = 'hello'.encode('UTF-8')
# q = queue.Queue(maxsize=0)
# q.put(item)
# q.put(item)
# q.put(item)
# q.put(item)
# def f():
#     print(s)
# s = "I hate spam"
# f()

# def foo(x, y):
#     global a
#     a = 42
#     x,y = y,x
#     b = 33
#     b = 17
#     c = 100
#     print(a,b,x,y)
#
# a,b,x,y = 1,15,3,4
# foo(x,y)
# print(a,b,x,y)

class A():
    def __init__(self):
        pass
class B():
    def __init__(self):
        b = A()


for i in range(0,10):
    b = B()
print('--')