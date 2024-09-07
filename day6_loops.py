# For Loop
for i in range(5):
    print(i)


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(1, 6):  # Loop from 1 to 5
    print(i)

# While loop

i = 0
while i < 5:
    print(i)
    i += 1

# infinite loops

while True:  # This will run forever unless stopped
    print("This is an infinite loop!")


# Loops control statements 

# break
for i in range(5):
    if i == 3:
        break  # Stops the loop when i equals 3
    print(i)

# Continue 

for i in range(5):
    if i == 3:
        continue  # Skips the iteration when i equals 3
    print(i)

# else in loops

for i in range(5):
    print(i)
else:
    print("Loop completed successfully.")

# Nested Loops

for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")


# Looping through dictionaries

student_grades = {"Alice": 85, "Bob": 90, "Charlie": 95}
for student, grade in student_grades.items():
    print(f"{student}: {grade}")


