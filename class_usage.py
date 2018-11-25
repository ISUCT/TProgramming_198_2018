import classes

test = classes.Car()
test.moveFwd()
print(test.fuel)
test.makeSound()
test.takePassanger()

test2 = classes.Car(10,2,43,50)
print(test2.x,test2.y, test2.speed, test2.fuel)
test2.__x = 5