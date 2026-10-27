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



human1 = Human("Rishi", 23, 'M')
print(human1.getName())
