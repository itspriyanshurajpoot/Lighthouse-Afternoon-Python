# Dictionary
# Ordered
# Mutable
# Homogeneous + Heterogeneous
# Keys cannot be dublicate


# Creating dictionary
# 1. Using {}

student1 = {
    "name" : "Rishi",
    "age" : 20,
    "courses" : ["SQL", "Python"],
    "address" : {
        "city" : "Pune",
        "state" : "Maharashtra",
        "pincode" : 111111
    },
    True: "Hello"
}



# Using dict()
student2 = dict(name="Rishi", age=23, courses=["SQL", "Python"])

print(student1, type(student1))
print(student2, type(student2))


# Access the element
print(student1["age"])

# Adding new key-value
student1["email"] = "priyanshu@gmail.com"
print(student1)

# Modify existing key value
student1["email"] = "rishi@gmail.com"
print(student1)

# Delete key value
# value = student1.pop('email1')
# print(value)

key, value = student1.popitem()
print(key, value, sep=":")
print(student1)


# Iterate
# First way to iterate
for element in student1:
    print(element, student1[element], end=" ")


print("-----------------------------------------")

print("Values", student1.values()) # ['Rishi', 20, ['SQL', 'Python'], {'city': 'Pune', 'state': 'Maharashtra', 'pincode': 111111}]
print("Keys", student1.keys())# ['name', 'age', 'courses', 'address']
print("Items", student1.items()) # [('name', 'Rishi'), ('age', 20), ('courses', ['SQL', 'Python']), ('address', {'city': 'Pune', 'state': 'Maharashtra', 'pincode': 111111})]


# Iterating over the values
for value in student1.values():
    print(value)

# Iterating over the keys
for key in student1.keys():
    print(key)

# Iterating over the items
for key, value in student1.items():
    print(key, value)


# In-built functions
keys = ["name", "age", "city"]
demoDict = student1.fromkeys(keys, "Unknown")
print(demoDict) # {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

