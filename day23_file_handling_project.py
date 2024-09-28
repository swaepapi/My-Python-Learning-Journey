# File handling Project.
# The project will involve creating a simple program that;
# Writes data to a file
# Reads the contents of the file
# Appends additional data to the file
# Implements error handling

def write_to_file(file_name, data):
    """
    Function to write data to a file.
    If the file already exists, it will overwrite the content.
    """
    try:
        with open(file_name, 'w') as file: # 'w' mode overwrites the file if it already exists
            file.write(data)
        print(f"Data written to {file_name}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def read_from_file(file_name):
    """
    Function to read and display the content of a file.
    Handles FileNotFoundError if the file doesn't exist.
    """
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            print(f"\nContents of {file_name}:\n{contents}")
    except FileNotFoundError:
        print(f"{file_name} not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file(file_name, new_data):
    """
    Function to append new data to an existing file.
    If the file doesn't exist, it will be created.
    """
    try:
        with open(file_name, 'a') as file:
            file.write(new_data)
        print(f"Data appended to {file_name}")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    # Define the file name
    file_name = "example.txt"
    
    # Step 1: Write initial data to the file
    data = "Welcome to the file handling project!"
    write_to_file(file_name, data)
    
    # Step 2: Read the content of the file
    read_from_file(file_name)
    
    # Step 3: Append new data to the file
    new_data = "\nThis project demonstrates file handling in Python."
    append_to_file(file_name, new_data)
    
    # Step 4: Read the content again to confirm the append
    read_from_file(file_name)

# Entry point of the script
if __name__ == "__main__":
    main()
