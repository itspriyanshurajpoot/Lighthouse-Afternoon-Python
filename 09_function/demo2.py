# global_var = "I am a global variable"

# def outer_function():
#     global global_var
#     global_var = "I am local to outer function"
#     print(global_var) # 1 I am local to outer function

#     def inner_function():
#         global global_var
#         global_var = "I am local to inner function"
#         print(global_var)  # 2.  I am local to inner function

#     inner_function()


# outer_function()
# print(global_var) # 3. I am local to inner function

# Closure : inner function remebers the enclosing variable's value
def outer_function(b):

    def inner_function(e):
        print(b ** e)

    return inner_function


inner_func1 = outer_function(10)
inner_func2 = outer_function(20)
inner_func1(2)
inner_func2(2)

# Lambda function
# def sum(a, b):
#     return a + b


sum = lambda a, b : a + b
value = sum(2, 3)
print(value)

