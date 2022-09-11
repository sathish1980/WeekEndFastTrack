from BasicsinPython.Encapsulation import Encapsulation


class Encapsulationotherpackage(Encapsulation):

    def __int__(self):
        pass

    def Bike(self):
        print("Max speed of bike is" , self.__maxspeed)

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed


obj=Encapsulationotherpackage()
obj.setMaxSpeed(180)
obj.Bike()