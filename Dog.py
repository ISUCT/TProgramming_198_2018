class Dog:

    def __init__(self, name="dog", age=1):
        self.__name= name
        self.__age = age
        pass

    def make_noize(self):
        print("Woof")
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age >0 and age<40:
            self.age = age
        else:
            print("Введите правильный возраст")
    

d1 = Dog("Sharik", 5)
d1.make_noize()
d1.set_age(5)
print(d1.get_name())

d2 = Dog("Bobik")
d2.set_age(150)
print(d2.get_name())