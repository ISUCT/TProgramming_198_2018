print("Hello world")
# Hello world
# Работа с числами и переменными
a = 2 + 3
print(a)
a = a + 2.4
print(a)
a *= 5 # a = a * 5
print(a)
a += float("2.2") + 5

print(8 % 3)

b = a - 18
print(a,b)

# Работа со строками
b = "Создаем строку - можно использовать - '' но \" \" предпочтительнее  "
print(b)
c = """
 Многострочная 
 строка
"""
print(c)

d = "Сложение " + "строк" 
print(d)

x = 5
y = 10
# Форматирование строк (без форматирования)
print("x="+str(x)+" y="+str(y))
# С форматированием
print("x=%1d y=%2d" % (x,y))

# Списки
a = [1,2,3,4,5]
print(a)
a = [1,2,3,"some string", [3,4]]
print(a)

wizard_list = ['паучьи лапки', 'жабий палец',
 'глаз тритона','крыло летучей мыши', 'жир слизня',
 'перхоть змеи']
print(wizard_list)

# обращение к элементам
print(wizard_list[0])
print(wizard_list[2])
print(wizard_list[0:3])
print(len(wizard_list))
print(wizard_list[len(wizard_list)-1])
print(wizard_list[-1])

print(a)
print(a[-1])
print(a[-2])
print(a[-2][0:4])
print('Not modified',a)

a[-2] = a[-2][0:4]
print('Modified',a)


fibs = (0, 1, 1, 2, 3)
print(fibs[1:3])

