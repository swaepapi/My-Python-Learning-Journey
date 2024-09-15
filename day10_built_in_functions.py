# Built in Functions 
#len() - Returns the length of an object

my_list = [1, 2, 3, 4]
print(len(my_list))  

# type(): Returns the type of an object.

print(type(10))  

# sum(): Returns the sum of all elements in an iterable (e.g., list, tuple).
numbers = [1, 2, 3, 4]
print(sum(numbers)) 

# max() and min(): Return the largest and smallest elements in an iterable.
print(max(numbers))  
print(min(numbers))  

# input(): Accepts input from the user.

name = input("Enter your name: ")
print(f"Hello, {name}")

# BUIT IN LIBRARIES

# math library
import math

#  square root of a number
print(math.sqrt(16))  # Output: 4.0

# Get the value of pi
print(math.pi)  # Output: 3.141592653589793

# Random Library
import random

# Generate a random integer between 1 and 10
print(random.randint(1, 10))

# Select a random item from a list
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))


# String Methods (Built-in)

# str.upper(): Converts a string to uppercase.
text = "sasa fidel"
print(text.upper()) 

#  str.lower(): Converts a string to lowercase.
print(text.lower())  

# str.replace(): Replaces occurrences of a substring with another subs
print(text.replace("a", "o"))  

# str.split(): Splits a string into a list based on a delimiter.
sentence = "Python is great"
print(sentence.split())  # Output: ['Python', 'is', 'great']

# Working with Lists (Built-in Functions)
# append 
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  

# remove 
my_list.remove(2)
print(my_list)  

# sort - sorts the list in ascending order 
my_list.sort()
print(my_list)  

# reverse - reverses order of elements 
my_list.reverse()
print(my_list)  

# Datetime library
import datetime

# Get the current date and time
now = datetime.datetime.now()
print(now)

# Format the date
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# File handling 
# Reading a file:
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a file:

with open('example.txt', 'w') as file:
    file.write("This is an example.")










