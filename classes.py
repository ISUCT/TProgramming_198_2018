class Vehicle:


    def __init__(self,x=0, y=0, speed=0,fuel=2):
        self.__x = x
        self.__y = y
        self.speed = speed
        self.fuel = fuel

    def getCoordinates(self):
        return self.__x

    def moveFwd(self):
        self.__x += 1
        self.speed += 5
        self.fuel -= 3
        pass

    def moveBwd(self):
        pass

    def turnLeft(self):
        pass

    def turnRight():
        pass

    def makeSound():
        pass

class Car(Vehicle):
    self.__type = ""

    def set_type(car_type):
        self.__type = car_type

    def get_type():
        return self.__type

    def makeSound(self):
        print("Wroom")

    def takePassanger(self):
        print("Wellcome onboard")

class Fox():
    def getView(self):
        return """
                                                                   ,-,
                                                             _.-=;~ /_
                                                          _-~   '     ;.
                                                      _.-~     '   .-~-~`-._
                                                _.--~~:.             --.____88
                              ____.........--~~~. .' .  .        _..-------~~
                     _..--~~~~               .' .'             ,'
                 _.-~                        .       .     ` ,'
               .'                                    :.    ./
             .:     ,/          `                   ::.   ,'
           .:'     ,(            ;.                ::. ,-'
          .'     ./'.`.     . . /:::._______.... _/:.o/
         /     ./'. . .)  . _.,'               `88;?88|
       ,'  . .,/'._,-~ /_.o8P'                  88P ?8b
    _,'' . .,/',-~    d888P'                    88'  88|
 _.'~  . .,:oP'        ?88b              _..--- 88.--'8b.--..__
:     ...' 88o __,------.88o ...__..._.=~- .    `~~   `~~      ~-._ Seal _.
`.;;;:='    ~~            ~~~                ~-    -       -   -
"""

if __name__ == '__main__':
    car1 = Car()
    car1.moveFwd()
    car1.moveFwd()

    lada = Car()
    lada.set_type("hatchback")
    lada.moveFwd()

    fox = Fox()
    print(fox.getView())