def f(n):
    return 3*n + 6

def g(n):
    return -2*n + 3

def h(n):
    return n**2

def doto(value, func):
    return func(value)

if __name__ == '__main__':
    print doto(7, f)
    print doto(7, g)
    print doto(7, h)
