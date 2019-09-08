import sys


def foo():
    print("module1 hello world")


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+ b
        print("gogogo")
        yield a

gen = fib(9)
# for x in gen:
#     print(x)


def print_letter(data):
    for index in range(len(data)):
        yield data[index]
g = print_letter("hello")


val = g.__next__()
try:
    while val:
        print(val)
        val = g.__next__()
except:
    pass

x = (1,2,3)
xx = [1,2,3]

print(sys.getsizeof(x))
print(sys.getsizeof(xx))