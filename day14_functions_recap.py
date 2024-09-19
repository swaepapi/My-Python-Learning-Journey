# A simple age calculator 
def greet_user(name):
    """Function to greet the user by name."""
    return f"Hello, {name}! Python is fun, Do you know that i can Calculate your age ."

def subtract_numbers(a, b):
    """Function to add two numbers and return the sum."""
    return b - a


def main():
    # Greet the user
    name = input("Enter your name: ")
    greeting = greet_user(name)
    print(greeting)

    # Add two numbers
    num1 = int(input("Enter your year of Birth: "))
    num2 = int(input("Enter the current Year: "))
    result = subtract_numbers(num1, num2)
    print(f"You are {result} years old.")

# Call the main function when the script is run
if __name__ == "__main__":
    main()
