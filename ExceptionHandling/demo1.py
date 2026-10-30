# Exception : It is an event/runtime error which disturbs the normal of program.

# Types of Error:
# 1. Compile time error
# 2. Logical error
# 3. Runtime error / Exception



try:
    a = int(input("Enter a number "))
    b = int(input("Enter second number "))

    print(a//b)

    list1 = [1, 2, 3, 4, "Hello"]
    print(list1[3]) 


except ValueError as e: 
    print(f"{type(e).__name__} : {e}")

except IndexError as e:
    print(f"{type(e).__name__} : {e}")

except ZeroDivisionError as e:
    print(f"{type(e).__name__}  : {e}")

except Exception as e:
    print(f"{type(e).__name__} : {e}")

else:
    print("I am else block, i will excute if no exception occurs")

finally : 
    print("I am finally block")


print("Hello")



