# Nested Dictionaries

students = {
    '001': {'name': 'Alice', 'age': 20, 'major': 'Physics'},
    '002': {'name': 'Bob', 'age': 22, 'major': 'Mathematics'},
    '003': {'name': 'Charlie', 'age': 23, 'major': 'Computer Science'}
}

# Accessing nested data
print(students['001']['name'])  # Output: Alice

# Dictionary Methods
# Using get() to avoid errors
person = {'name': 'John', 'age': 30}
print(person.get('age'))  # Output: 30
print(person.get('gender', 'Not specified'))  

# Using update() to merge dictionaries
additional_info = {'gender': 'Male', 'occupation': 'Engineer'}
person.update(additional_info)
print(person)  

# Getting all items, keys, and values
print(person.items())    
print(person.keys())    
print(person.values())  

# Dictionary Comprehension
# Creating a dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtering a dictionary
even_squares = {x: x**2 for x in range(1, 6) if x % 2 == 0}
print(even_squares)  

# Working with Dictionaries and Functions
# Function to update a student’s age
def update_age(students, student_id, new_age):
    if student_id in students:
        students[student_id]['age'] = new_age
    else:
        print("Student ID not found.")
    
students = {
    '001': {'name': 'Alice', 'age': 20, 'major': 'Physics'},
    '002': {'name': 'Bob', 'age': 22, 'major': 'Mathematics'}
}

update_age(students, '001', 21)
print(students['001'])  
