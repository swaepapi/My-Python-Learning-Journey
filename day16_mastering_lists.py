# Creating lists with multiple data types 
mixed_list = [1, "Hello", 3.14, True, [5, 6]]
print(mixed_list)

# Accessing Elements in a Mixed List

print(mixed_list[1])  

print(mixed_list[4])  
# Access an element inside the nested list
print(mixed_list[4][1])  

# Modifying List Elements
mixed_list[0] = "New Value"
print(mixed_list)  

# Add an element
mixed_list.append(False)
print(mixed_list)  

# Remove an element
mixed_list.remove("Hello")
print(mixed_list)  

# Slicing list 
sliced_list = mixed_list[1:4]
print(sliced_list)  

# Using in Operator:  to check if a value exists in the list.
if "New Value" in mixed_list:
    print("Found!")

# Combining lists
new_list = ["swae", 99]
combined_list = mixed_list + new_list
print(combined_list)




