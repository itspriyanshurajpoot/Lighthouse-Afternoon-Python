# List : 
# It is a sequence data type
# Mutable
# Ordered
# Follow indexing
# Allow dublicates
# It can be nested
# Allow homogeneous as well as heterogeneous

# Creating list
my_list1 = [2, 3, "Hello", True]
my_list1 = list([2, 3, "Hello", True])


# Nested list

data = [100, "Python",[ 200, "Java",[ 300, "Spring Boot", [ 400, "MongoDB"]]]]

# Accessing elements
# 1. Index
print(data[2][2][2][0])

# 2. Slicing
my_list1 = [2, 3, "Hello", True, 100, 200, 300, 400, [500, 600, 700, 800, [900, 1000]]]
print(my_list1[8][3::])

# Adding elements with the help of three methods
# 1. append(x) --> It will add the element x at last of list
l1 = [1, 2, 3, 4, 5]
l1.append(100)
print(l1) # [1, 2, 3, 4, 5, 100]

# 2. insert(index, element) --> It will add the element at the given index.
l1.insert(2, 50)
print(l1) # [1, 2, 50, 3, 4, 5, 100]

# 3. extend(x) --> add multiple elements at last of the list
l1.extend([300, 400, 500])
print(l1) # [1, 2, 50, 3, 4, 5, 100, 300, 400, 500]

l1.append([1000, 2000])
print(l1) # [1, 2, 50, 3, 4, 5, 100, 300, 400, 500, [1000, 2000]]

# Modify
# 1. Indexing
l1[0] = 10
print(l1) # [10, 2, 50, 3, 4, 5, 100, 300, 400, 500, [1000, 2000]]

# 2. Slicing
l1 = [1, 2, 5,6, 9, 1]
print(l1) # [1, 2, 5, 6, 9, 1]
l1[2:4:1] = 50, 60
print(l1) # [1, 2, 50, 60, 9, 1]

# Deleting elements using three methods
# 1. remove(x) : It will delete the first occurence of the given element
l1.remove(1)
print(l1) # [ 2, 50, 60, 9, 1]

# l1.remove(100) : It will raise ValueError because 100 is not present in l1
# print(l1)

# 2. pop(index) # It will delete the element present at the given index, if index is not passed, it will delete the last element and return it.
value = l1.pop(0)
print(value, l1) # 2 [50, 60, 90, 1]

value = l1.pop()
print(value, l1) # 1 [50, 60, 9]

# clear()
l1.clear() 
print(l1) # []

del l1 # It will delete the l1 from memory
# print(l1)

# In-built functions
l1 = [1, 2, 8, 1, 3, 4, 5, 5]
print(l1.count(5)) # 2
l1.sort()
print(l1) # [1, 1, 2, 3, 4, 5, 5, 8]
l1.sort(reverse=True)
print(l1)
