class Human:
    def __init__(self, name, age, gender): # Constructor : It is a special function which called during the object creation, the main purpose of creating constructor is to initialize the instance variable.
        self.__name = name
        self.__age = age
        self.gender = gender
        
    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def __str__(self): # To string : It returns the string representation of an object
        return f"Namee is {self.__name}, Age is {self.__age}, Gender is {self.gender}"





class Car:
    def __init__(self, color, speed, milage, brand, engineType):
        print(" I am Car class")
        self.color = color
        self.speed = speed
        self.milage = milage
        self.brand = brand

    def getBrand(self):
        print(self.brand)

    def __str__(self):
        return f"Color is {self.color}, Speed is {self.speed}, Milage is {self.milage} and Brand is {self.brand}"


class BMW(Car):
    def __init__(self, color, speed, milage, brand, engineType):
        self.speed = speed
        self.color = color
        self.brand = brand
        self.milage = milage
        self.engineType = engineType

    def getBrand(self):
        print(f"Brand name is {self.brand}")

    def drift(self):
        print("Drifttt.....")

    def __str__(self):
        return f"Color is {self.color}, Speed is {self.speed}, Milage is {self.milage}, Brand is {self.brand} and Engine Type is {self.engineType}"

car1 = BMW("Red", 300, 10, "BMW","Petrol")
car1.getBrand()
car1.drift()
print(car1)

car2 = Car("Blue", 200, 10, "Audi", "Battery")
car2.getBrand()
print(car2)


