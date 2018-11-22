import math

def calc(a,b,x):
    chisl = a * x**(1/3.0) - b* math.log(x, 5)
    znam = (math.log(x-1)**3)
    y = chisl/znam
    return y

def full_calc(a, b, xn, xk, dx):
    x = xn
    while x < xk:
        res = calc(a,b,x)
        print("x=%2.2f y=%2.2f" % (x, res))
        x = x+dx

full_calc(4.1, 2.7, 1.5, 3.5, 0.4)

print((8+19)**(1/3))

8**(1/3)

