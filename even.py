i = -10
while i < 11:
    if i == 0:
        print("Ноль")
    elif i % 2 == 0: # if i % 2:
        print("Четное")
    else:
        print("Нечетное")
    i = i + 1 # i += 1 

print("--------------------------")
for i in range(0,10):
    if i % 2 == 0: # if i % 2:
        print("Четное")
    else:
        print("Нечетное")

print("x=%s" % 1)

for x in range(0, 20):
    if x > 9 and x < 15:
        continue
    print('привет %s' % x)

ingredients = ['слизни', 'пиявки', 'катышки из пупка гориллы',
'брови гусеницы', 'пальцы многоножки']

x = 1
for i in ingredients:
    print(x, i)
    x = x + 1

for i in range(0, len(ingredients)):
    print(i+1, ingredients[i])

s = "ajs\r\n djadgj\t'ajsdnjasndj \" nasdfn asndf"
print(s)
print(len(s))
# for i in range(0,len(s)):
#     print(i+1, s[i])

# 1 x 1 = 1

