# Take two number from the user, add it and display the output


# x = float(input("Enter first number : "))
# y = int(input("Enter the second number : "))

# sum = x + y

# print(sum)

# Homework: Write a program to add, subtract, multiply and divide two numbers

# String formatting
name = "Raj"
age = 30

day = 15
month = 10
year = 2026
# My name is-Raj-and age is-30
# 15/10/2026
# Comma
print("My name is", name, "and age is", age, sep=" ", end="\n")
# print(day, month, year, sep="/")

# Concatenation
print("My name is " + name + " and age is " + str(age))

# % Formatting
print("My name is %s and age is %d"%(name, age))

# str.format
print("My name is {} and age is {}".format(name, age))

# f-string
print(f"My name is {name} and age is {age}")