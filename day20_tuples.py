#Tuples
# A tuple with multiple elements
my_tuple = (1, 2, 3, "hello", 5.0)

# A tuple with one element (note the comma)
single_element_tuple = (10,)

# Tuple Unpacking

a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3

# Tuple Methods 

my_tuple = (1, 2, 3, 1, 1)
print(my_tuple.count(1))  # (counts how many times 1 appears)
print(my_tuple.index(2))  #  (index of first occurrence of 2)


# Sets

# creating a set
# A set with multiple elements
my_set = {1, 2, 3, 4, 4}  #  (duplicates removed)

# An empty set
empty_set = set()  # You must use the set() constructor


# Adding and Removing Elements

my_set.add(5)   
my_set.remove(3)  # Removes 3 from the set (throws an error if 3 is not present)
my_set.discard(4)  # Removes 4 but won't throw an error if 4 is not present

# Set operations

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (all unique elements from both sets)
print(set1.union(set2))  

# Intersection (common elements between both sets)
print(set1.intersection(set2))  

# Difference (elements in set1 but not in set2)
print(set1.difference(set2))  

# checking if an element exists in a set

print(2 in set1)  
print(4 in set1)  

