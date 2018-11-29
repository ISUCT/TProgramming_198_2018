file = open("sample", "w")
str_to_write = """Hello world
asdhfja hsdjfh asdf kjahsdfj
asdf hajsdhf jasdfjk asdf
asdjf jashdfja hsdfj h
asdjfh jasdhfjhjh asdf
"""
file.write(str_to_write)
file.write("New string")
file.close()

file = open("calc.txt", "w")

x = """1
2.1
3.3
4.5
5
"""
file.write(x)
file.close()

file = open("calc.txt", "r")
res = file.readlines()
print(res)
file.close()

file = open("calc.txt", "r")
X = []
while True:
    x_str = file.readline()
    if x_str:
        x = float(x_str)
        X.append(x)
        print(x)
    else:
        break
file.close()
print(X)

print(res)
X1 = [float(i) for i in res if float(i)>3 ]
print(X1)