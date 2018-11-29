def fact(n): # вычисление факториала без рекурсии
    if n:
        res = 1
        for i in range(1,n+1):
            res = res * i
        return res
    return 1

def fact1(n): # реализация с использованием рекурсии
    if n <= 1:
        return 1
    temp = n*fact1(n-1)
    return temp

res = fact1(5)
print(res)