def summ(a, b, c):
    return a+b-c

def table(n=10,m=10):
    for x in range(1,n+1):
        for y in range(1,m+1):
            mul = x * y
            print("%d x %d = %d" % (x,y,mul))

# summ(2,3,1)
# summ(5,2,2)
# summ(5,6,3)

# table(2,3)
# # table(150,150)
# table(15,5)

a = 3
b = 4
# table(a,b)
# table(n=a,m=b)
# table(m=b,n=a)
# table()
# table(2)
# table(m=2)
# table(n=3)

result = summ(2,3,4)
print(result)