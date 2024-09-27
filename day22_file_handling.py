# File handling 

# Opening a File
# Open a file for reading
file = open('myFile.txt', 'r')

# Always remember to close the file after
file.close()

# Reading from file 
# Reading the entire content
file = open('myFile.txt', 'r')
content = file.read()  # Reads the entire file
print(content)
file.close()

# Wrting into the file 

# Writing to a file (overwriting the content)
with open('myFile.txt', 'w') as file:
    file.write("Hello, Fidel!\n")
    file.write("Writing to files in Python is fun!\n")


# Appending to a file
with open('myFile.txt', 'a') as file:
    file.write("This will be added to the end.\n")

#  File Handling with Exception Handling

try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")


#  Working with File Paths

import os

if os.path.exists('myFile.txt'):
    print("File exists")
else:
    print("File does not exist")



# Example
# Step 1: Writing to the file
try:
    with open('data.txt', 'w') as file:
        file.write("Line 1: This is the first line.\n")
        file.write("Line 2: Learning file handling in Python.\n")
        file.write("Line 3: Python makes this easy!\n")
    print("Data successfully written to 'data.txt'.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# Step 2 and 3: Reading from the file and handling errors
try:
    with open('data.txt', 'r') as file:
        print("Reading file content line by line:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file you are trying to read does not exist.")
except PermissionError:
    print("Error: You don't have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
