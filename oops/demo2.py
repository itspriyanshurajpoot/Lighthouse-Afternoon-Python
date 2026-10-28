class A:
    def __init__(self):
        print("Class A constructor")


class B:
    def __init__(self):
        print("Class B constructor")


class C(A, B):
    def __init__(self):
        B.__init__(self)



class Human:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender


class Student(Human):

    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    @classmethod
    def defineInstitute(cls, instituteName):
        cls.instituName = instituteName

    @classmethod
    def displayInstitute(cls):
        print(cls.instituName)

    def getName(self):
        print(f"My name is {super().getName()}")

    
    def __str__(self):
        return f"Name is {self.getName()}, Age is {self.getAge()}, Gender is {self.getGender()} and Student id is {self.student_id}"



# priyanshu = Student("Priyanshu", 22, 'M', 101)
# print(priyanshu.getAge())
# priyanshu.getName()

Student.defineInstitute("SEED")
Student.displayInstitute()

from abc import ABC, abstractmethod

class PaymentService(ABC):

    def checkBalance():
        print("I am checking")

    @abstractmethod
    def withdraw():
        pass


class UPIPayementService(PaymentService):

    def withdraw():
        print("I am withdrawing...")

UPIPayementService()