#Function Arguments and parameters
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet(name="Fidel", message="Welcome"))

#Arbitrary Arguments
#args
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Output: 10

#Kwags
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Fidel", age=25, role="Developer")

# Retuen Multiple Values from a function
def get_user_info():
    name = "Fidel"
    age = 25
    return name, age

user_name, user_age = get_user_info()
print(user_name, user_age)

# Lambda functions
square = lambda x: x * x
print(square(5))  # Output: 25


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Recurssion 
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120

# Scope and lifetime of variables

x = 10  # Global scope

def show_number():
    global x
    x = 20  # Modifies the global variable
    print(x)

show_number()
print(x)  # Output: 20

# Decorators 
def decorator_function(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator_function
def say_hello():
    print("Hello, world!")

say_hello()

# High order Functions

def higher_order_func(func, value):
    return func(value)

result = higher_order_func(lambda x: x + 5, 10)
print(result)  # Output: 15
