


# Functions

# Declare the function

def takeInput():
    num1 = int(input("Enter first number "))
    num2 = int(input("Enter second number "))

    return num1, num2

def add(num1, num2):
    print("Sum is ", (num1 + num2))


def sub():
    num1, num2 = takeInput()
    print("Subtraction is ", (num1 - num2))



# choice = int(input("Press 1 for addition\nPress 2 for subtraction"))
# if choice == 1:
#     # num1, num2 = takeInput()
#     add(50, 100)

# elif choice == 2:
#     sub()

# else:
#     print("Invalid choice")

# Named Argunment
def display(name, age):
    print(name, age)

display(age=20, name="ABC")

# Arbitrary variable length argunment
def sum1(*value):
    sum = 0
    for element in value:
        sum += element

    print("Sum is ", sum)

sum1(3, 4, 5, 6)

# Arbitrary key worded argunment
def displayDict(**value):
    for key, val in value.items():
        print(key, val, sep=":")

displayDict(name="Rishi", age=20)

