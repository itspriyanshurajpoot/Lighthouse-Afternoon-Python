# Question : 1

# # Addition
# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number "))

# choice = int(input("Press 1 for addition"))


# if choice == 1 :
#     sum1 = num1 + num2
#     print("Sum is ", sum1)

# else :
#     minus = num1 - num2
#     print("Subtraction is ", minus)

# Question 2: Check a number is even or odd
# num = int(input("Enter a number to check even or odd "))

# if num % 2 == 0 :
#     print("Even number")

# else :
#     print("Odd number")

# Question 3: Find the simple interest but the rate of interest will depend on gender
# Male : 8%
# Female : 6%

# principal = float(input("Enter the amount "))
# time = float(input("Enter the time (in year) "))
# gender = input("Enter your gender ")

# if (gender == 'Male'):
#     si = principal * time * 8 / 100
#     print(f"Simple intrest is {si}")

# else:
#     si = principal * time * 6 / 100
#     print(f"Simple intrest is {si}")

# Question 4: Display the grade according to the marks
# marks >= 90 ---> Grade A
# 90 > marks >= 80 --> Grade B
# 80 > marks >= 60 --> Grade C
# 60 > marks >= 40 --> Grade D
# Else Grade E

marks = int(input("Enter your marks "))

if marks >= 90:
    print("Grade A")

elif marks >= 80 : 
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40 :
    print("Grade D")

else :
    print("Grade E")