# Lists
# Indexing and Slicing

fruits = ['apple', 'banana', 'cherry', 'orange', 'mango']

# Indexing
first_fruit = fruits[0]     
last_fruit = fruits[-1]      

# Slicing
sublist = fruits[1:4]        
reversed_fruits = fruits[::-1] 

print(first_fruit, last_fruit)
print(sublist)
print(reversed_fruits)

# List Methods: Adding and removing elements using common list methods.

tasks = ['Read Python book', 'Write code', 'Test project']

# Adding tasks
tasks.append('Review project')  
tasks.insert(1, 'Learn Power BI') # Inserts  at index 1

# Removing tasks
tasks.remove('Write code')  
finished_task = tasks.pop(2) # Removes and returns the item at index 2

print(tasks)         
print(finished_task) 

# List Comprehensions
numbers = [1, 2, 3, 4, 5, 6]

# Double each number in the list
doubled = [x * 2 for x in numbers]

# Filter even numbers
evens = [x for x in numbers if x % 2 == 0]

print(doubled)  
print(evens)    


# Nested Lists

# List of coordinates (x, y)
coordinates = [[1, 2], [3, 4], [5, 6]]

# Accessing the first x and y coordinate
first_x = coordinates[0][0]  
first_y = coordinates[0][1]  

# Modifying a coordinate
coordinates[1][0] = 7  # Updates second x-coordinate to 7

print(first_x, first_y)
print(coordinates)  

# Copying Lists

import copy

# Original list
original = [[1, 2], [3, 4], [5, 6]]

# Shallow copy
shallow_copy = original.copy()

# Deep copy
deep_copy = copy.deepcopy(original)

# Modifying the original list
original[0][0] = 10

#how the changes affect the copies
print(f"Original: {original}")        # [[10, 2], [3, 4], [5, 6]]
print(f"Shallow Copy: {shallow_copy}") # [[10, 2], [3, 4], [5, 6]]
print(f"Deep Copy: {deep_copy}")       # [[1, 2], [3, 4], [5, 6]]


# Mutable lists

# List of temperatures in degrees Celsius
temperatures = [20, 22, 24, 19, 21]

# Update the temperature at index 3
temperatures[3] = 23

# Append a new temperature reading
temperatures.append(25)

print(temperatures)  # [20, 22, 24, 23, 21, 25]


# Using sort and reverse
# List of ages
ages = [25, 18, 30, 22, 21]

# Sort the list in ascending order
ages.sort()

# Reverse the sorted list
ages.reverse()

print(ages)  # [30, 25, 22, 21, 18]
