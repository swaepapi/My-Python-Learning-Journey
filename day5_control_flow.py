# Conditional Statements 
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# Loops: For and while

# For Loop

fruits = ["apple", "banana", "cherry", "mango", "oranges"]
for fruit in fruits:
    print(fruit)


# While

count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

# Breaking out Loops

# Break

for i in range(10):
    if i == 5:
        break
    print(i)


# Continue

for i in range(5):
    if i == 2:
        continue
    print(i)

# Nested Loops and conditionals

for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            print(f"{i} equals {j}")
        else:
            print(f"{i} does not equal {j}")
