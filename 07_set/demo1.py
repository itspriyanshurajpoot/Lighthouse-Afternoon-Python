# Set
# Mutable
# Unique element
# Unordered
# Homogeneous + Hetergeneous
# Doesn't allow indexing


# Creating set
my_set1 = {1, 2, 3, 4, True, "Hello", 0, "World", False, (3, 4, 5)}
my_set2 = set([2, 3, 4, 2])

print(my_set1)
print(my_set2)


# Adding elements
my_set2.add(100)
print(my_set2)

my_set2.update((2, 3, 4, 1))
print(my_set2)

# Deleting element
my_set2.remove(100) 
print(my_set2)

my_set2.discard(200)
print(my_set2)

# my_set2.clear()
# print(my_set2)

# Iterating
for element in my_set2:
    print(element)

# Membership operator
if 30 in my_set2:
    print("Element is present")

# Operation on set
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Union 
print(A | B) # 1, 2, 3, 4, 5, 6
A.union(B) # 1, 2, 3, 4, 5, 6


# Intersection
print(A & B) # 3, 4
A.intersection(B) # 3, 4

# Difference
print(A - B) # 1, 2
A.difference(B) # 1 2


# Symmetric difference
print(A ^ B) # 1, 2, 5, 6
A.symmetric_difference(B) # 1, 2, 5, 6

# Subset
print(A.issubset(B)) # False
print(B.issuperset(A)) # False

C = {1, 2}
D = {3, 4}
print(C.isdisjoint(D)) # True