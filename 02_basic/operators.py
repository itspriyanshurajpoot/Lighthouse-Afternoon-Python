# Arithmatic Operator : +, -, *, /, //, %, **
print(10 + 20) # 30
print(20 - 10) # 10
print(10 * 10) # 100
print(5 / 2) # 2.5
print(5 // 2) # 2
print(5 % 2) # 1
print(2 ** 2) # 4

# Assignment operator
# x += y --> x = x + y
# x -= y --> x = x - y
# x *= y --> x = x * y
# x /= y --> x = x / y
# x //= y --> x = x // y
# x %= y --> x = x % y
# x **= y --> x = x ** y

x = 10
y = 20
x += y
print(x)

# Comparison operator : ==, !=, >, >=, <, <=

# Bitwise : (AND)&, (OR)|, (NOT)~, (XOR)^, (Right shift)>>, (Left shift)<< 
print(181 >> 2)

# Identiy operator: is, is not

# Mutable
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y) # F
print(x is z) # T

# Immutable
x = (1, 2, 3)
y = (1, 2, 3)
print(x is y)

# Membership operator : in , not in
a = 2
print(a in x) # T
print(5 in x)