a = 8
if a >= 9 and a <= 20:
    print("Hello")
else:
    print("Bye")
print(a==9)

vozrast = -5
if vozrast < 6 and vozrast>=0:
    print("Дошкольник")
elif vozrast >=6 and vozrast <=18:
    print("Школьник")
elif vozrast >18 and vozrast <=25:
    print("Студент")
    print("Дополнительное образование")
elif vozrast <0 or vozrast >=150:
    print("Не правильно введены данные")
else:
    pass
    print("Человек")

# and or not
print(10+5)

for i in range(0,5,2):
    print("Hello", i)

print(list(range(0,5)))

a = [3,4,6,9]
for znachenie in a:
    print(znachenie)

b = "Some string asdfh gashf ahjsf h"
for i in b.split(" "):
    print(i)

i=0
while i<10:
    print("i=%d" % i)
    i = i + 1



