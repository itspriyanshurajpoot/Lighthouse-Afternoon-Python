# Keywords : Keywords are those words having a predefined meaning.
# We cannot change the meaning of keywords.

# This code will print the list of keywords

import keyword
# print(keyword.kwlist)

# Identifiers : Identifiers are basically some name (name of variable, functions, classes, and other user defined objects) which help us to identify something.

# Rule of identifiers
# 1. Cannot use keywords
# 2. Use A-Z, a-z, 0-9, _
# 3. Cannot use special characters like &, $, #, etc 
# 4. We cannot use space


# Variable : It is an identifier which referes a memory location in out memory.

name = "ABC"
num1 = 20
num2 = 20.5
isPrime = True



# print("My name is", name)
# print("My name is", name)
# print("My name is", name)
# print("My name is", name)
# print("My name is", name)


# Data types : int, float, complex, dictionary, boolean, set, string, list, tuple

# List : Ordered, Mutable, Dublicates, Indexing
# Tuble : Ordered, Immutable, Dublicates, Indexing
# Set : Unordered, Mutable, Unique elements, No-indexing

age = 21
salary = 38232.5
cmpNum = 2 + 5j
student = {
    "name" : "Subham",
    "age" : 21,
    "gender" : 'M'
}
isPrime = True
my_set = {88, 87, 45, 90, True, 2+5j, 88}
my_list = [88, 87, 45,100, 90, True, 2+5j]
my_tuple = (88, 87, 45, 90, True, 2+5j)
name = "Subham"


print(age, type(age)) # type() is used to find the data type of a variable

my_list.append(100)
print(my_list)

print("Set", my_set)

# Data type conversion (Type casting): Converting the data type of a value from one to another data type
# There are two types of Type casting:
# 1. Implicit : Convertion automatically done by the python
x = 10
y = 20.5
z = x + y
print(z, type(z)) # 30.5, float

# 2. Explicit : Python doesn't convert automatically, we have to convert manually.
name = "ABC"
age = 20
msg = "My name is " + name + " and age is " + str(age)
print(msg)


# int(x) --> Convert the x into integer
# float(x) --> Convert the x into float  
# complex(x) --> convert the x into complex
# list(x) --> convert x into list
# tuple(x) --> convert x into tuple
# str(x) --> convert x into string
# set(x) --> convert x into set
# dict(x) --> convert x into dictionary
# bool(x) --> convert x into boolean
