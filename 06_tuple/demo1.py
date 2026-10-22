# Tuple
# Sequence data type
# Immutable
# Allow dublicates
# Ordered
# Homogeneous and Heterogeneous
# Allow indexing

# Creating tuples
my_tuple1 = (1, 2, 3, 4, 5)
my_tuple2 = tuple([3, 4, 5, 2, "Hello"])


print(my_tuple1, type(my_tuple1))
print(my_tuple2, type(my_tuple2))

# Nested tuple
my_tuple3 = (1, 2, 3, 4, 5, ("Hello", True))

# Accessing elements
# 1. Indexing
print(my_tuple3[5][1])

# 2. Slicing
print(my_tuple3[5:2:])

# Iterating
for index, element in enumerate(my_tuple3):
    print(index, element, sep=":")


# Concatination
print(my_tuple1 + my_tuple2)

# Repitation
print(my_tuple1 * 2)


# Packing and Unpacking
a = 2, 3, 4, "Hello"
print(a, type(a))

b, c, d, e = a
print(f"b is {b}, c is {c}, d is {d}, e is {e}")

# Inbuilt functions
my_tuple4 = a = 2, 3, 4, 2, "Hello"
print(my_tuple4.count(2))
print(my_tuple4.index(2, 1))
