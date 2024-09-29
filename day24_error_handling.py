# Basic try-except Block

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You can't divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

#  Catching Multiple Exceptions

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"Result: {result}")
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")

# Using else and finally Blocks

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Error: You can't divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print(f"Result: {result}")
finally:
    print("Program finished.")

# Raising Your Own Exceptions

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    else:
        print("Age is valid.")

try:
    check_age(15)
except ValueError as e:
    print(f"Error: {e}")


# Applying Error Handling to File Operations
# Using my perevious project 

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Attempt to read file completed.")

# Try to read from a file that doesn't exist
read_file('non_existing_file.txt')


# Writing to a File with Error Handling

def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            file.write(data)
            print(f"Data written to {file_name}")
    except IOError:
        print(f"Error: Could not write to file '{file_name}'.")
    finally:
        print("Attempt to write to file completed.")

# Try to write data to a file
write_to_file('output.txt', 'Hello, Python!')

