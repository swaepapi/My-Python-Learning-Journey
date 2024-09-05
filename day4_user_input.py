name = input("Enter your name: ")
print (f"Hello, {name}!")

# Handling different data types

age = input("Enter your age: ") 
age = int(age)
print(f"You are {age} years old.")

# performing operations on user input

first_half = float(input("Enter the first half score: "))
second_half = float(input("Enter the second half score: "))
result = first_half + second_half
print(f"The Full time score  is: {result}")

# Error handling with user input
try:
    first_half = float(input("Enter the first half score: "))
    second_half = float(input("Enter the second half score: "))
    result = first_half + second_half
    print(f"The Full time score  is: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")


# A simple calculator

print("A basic calculator!")
operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()

if operation == "add":
    first_half = float(input("Enter the first half score: "))
    second_half = float(input("Enter the second half score: "))
    result = first_half + second_half
    print(f"The Full time score  is: {result}")
elif operation == "subtract":
    first_half = float(input("Enter the first half score: "))
    second_half = float(input("Enter the second half score: "))
    print(f"The result is: {first_half - second_half}")
# Similarly, you can add cases for multiplication and division
else:
    print("Invalid operation!")


