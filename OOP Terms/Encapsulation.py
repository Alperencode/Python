#%%
class Car:
    def __init__(self):
        self.__speed = 0

    def setSpeed(self,speed):
        self.__speed = speed
    
    def getSpeed(self):
        return self.__speed

x = Car()

print("First speed:",x.getSpeed())

x.setSpeed(100)

print("Secon speed:",x.getSpeed())


