# A list in Python is a collection of items that are ordered and mutable (changeable).

# Empty list
my_list = []

# List with integers
int_list = [1, 2, 3, 4]

# List with strings
str_list = ["apple", "banana", "cherry"]

# List with mixed data types
mixed_list = [1, "hello", 3.14, True]

# Accessing List Elements

# Access the first element
print(mixed_list[0])  # Output: 1

# Access the third element
print(mixed_list[2])  # Output: 3.14

# You can also access elements from the end of the list using negative indexing:

# Access the last element
print(mixed_list[-1])  # Output: True

# Access the second-to-last element
print(mixed_list[-2])  # Output: 3.14

# Moddifying Lists

my_list = [1, 2, 3, 4]
my_list[1] = 100  
print(my_list)  

#Appending 
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  

# Inserting into a specific position

my_list.insert(1, 'inserted')  # Insert 'inserted' at index 1
print(my_list)  

# Removing elements - remove,pop,delete

my_list.remove(2)  
print(my_list)  

my_list.pop()  
print(my_list)  

