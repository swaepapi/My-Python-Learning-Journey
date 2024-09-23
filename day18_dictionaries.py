# A simple dictionary
student = {
    'name': 'Fidel',
    'age': 25,
    'course': 'Software Engineering'
}
print(student)

# Accessing the value of a key
print(student['name'])  

# Modifying the value of an existing key
student['age'] = 24
print(student)  

# Adding a new key-value pair
student['grade'] = 'A'
print(student)  

# Removing Items from a Dictionary
# Using pop()
age = student.pop('age')
print(age)  
print(student)  

# Using del
del student['course']
print(student)  

# Using popitem() (removes the last added key-value pair)
student.popitem()
print(student)  



# Looping Through Dictionaries

# Looping through keys
for key in student:
    print(key)

# Looping through values
for value in student.values():
    print(value)

# Looping through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")


# Dictionaries length

print(len(student))  

