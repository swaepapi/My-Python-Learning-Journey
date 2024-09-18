# expense_calculator.py

# Dictionary to store expenses by category
expenses = {}

def add_expense(category, amount):
    """Adds an expense to the specified category."""
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def view_expenses():
    """Displays all expenses by category."""
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")

def get_total_expenses():
    """Returns the total expenses."""
    total = sum(expenses.values())
    return total

def is_valid_amount(amount_str):
    """Checks if the input string is a valid float for amount."""
    try:
        float(amount_str)
        return True
    except ValueError:
        return False

def main():
    print("Welcome to the Expense Tracker!")
    
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Get Total Expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category (e.g., food, transport): ")
            amount_str = input("Enter amount: ")

            if is_valid_amount(amount_str):
                amount = float(amount_str)
                add_expense(category, amount)
                print(f"${amount:.2f} added to {category} category.")
            else:
                print("Invalid amount. Please enter a number.")

        elif choice == '2':
            print("\nYour Expenses:")
            view_expenses()

        elif choice == '3':
            total = get_total_expenses()
            print(f"\nTotal Expenses: ${total:.2f}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
