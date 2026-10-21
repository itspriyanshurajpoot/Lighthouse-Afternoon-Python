# String :
# It is in-build class "str"
# Immutable
# Sequence
# Ordered
# Collection of characters hold. (one or more character)

# Creating string
str1 = "Rishi"
str2 = 'Rishi'
str3 = ''' Arpit '''
str4 = """ Arpit """
str5 = str(273)

print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))
print(str5, type(str5))


# Accessing element
# 1. Indexing
print(str1[2])
print(str1[-2])

# 2. Slicing
value = "SEED Infotech"
print(value[8:11:1]) # ote
print(value[8:11:]) # ote
print(value[:11:]) # SEED Infote
print(value[:11:-1]) # SEED Infote
print(value[::-1]) # hcetofnI DEES
print(value[5::]) # Infotech


# Iterating
value = "SEED Infotech"

# Immutable
# value[3] = 'E'

for ch in value:
    ascii = ord(ch)

    if ascii >= 65 and ascii <= 90:
        print(ch, end=" ")


# Comparing string

str1 = "Mani"
str2 = "mani"

# Compare memory address (is)
print(str1 is str2)
print(str1 is not str2)

# Compare content (==)
print(str1 == str2)
print(str1 != str2)


# Escape sequence
print("Hel\tlo")
print("Hel\nlo")


# String formatting
name = "Vaishnavi"
age = 25

# My name is Shreya and age is 30
# Comma
print("My name is", name, "and age is", age, sep="-")

# Concatination
print("My name is " + name + " and age is " + str(age))

# % formatter
print("My name is %s and age is %d"%(name, age))

# str.format
print("My name is {} and age is {}".format(name, age))

# f-format
print(f"My name is {name} and age is {age}")


# Inbuilt-functions in String
value = "SEED Infotech"


# String inbuilt functions
print(value.upper())
print(value.lower())
print(value.capitalize())
print(len(value))
print(value.count('E'))
print(value.endswith('h'))
print(value.startswith('S'))


