
#  Nested Data Structures: A Dictionary of Lists

# Dictionary of students with their grades in different subjects
student_grades = {
    'John': [85, 78, 92],
    'Sarah': [91, 88, 84],
    'Mike': [79, 94, 90]
}

# Calculate the average grade for each student
for student, grades in student_grades.items():
    avg_grade = sum(grades) / len(grades)
    print(f"{student}'s average grade is {avg_grade:.2f}")

# Tuples as Dictionary Keys: Handling Complex Data

# Tuple of coordinates as keys, with city names as values
city_locations = {
    (34.05, -118.25): "Los Angeles",
    (40.71, -74.01): "New York",
    (51.51, -0.13): "London"
}

# Find a city by its coordinates
coordinates = (40.71, -74.01)
city = city_locations.get(coordinates, "Unknown location")
print(f"The city at coordinates {coordinates} is {city}.")


# Using Sets to Handle Uniqueness
# List of students' names (some are duplicates)
students = ['John', 'Sarah', 'Mike', 'John', 'Sarah']

# Use a set to find unique students
unique_students = set(students)
print(f"Unique students: {unique_students}")


# Combining Data Structures: A Real-World Example

# A list of dictionaries where each entry maps a product (tuple) to its available stores (set)
inventory = [
    {('Laptop', 'HP'): {'Store1', 'Store3', 'Store5'}},
    {('Phone', 'Samsung'): {'Store1', 'Store4'}},
    {('Tablet', 'Apple'): {'Store2', 'Store3'}}
]

# Example: Find all stores where 'Laptop' of brand 'HP' is available
for item in inventory:
    product = ('Laptop', 'HP')
    if product in item:
        stores = item[product]
        print(f"The {product[1]} {product[0]} is available in: {', '.join(stores)}")


# Building a Custom Data Structure: A Mini-Project
# A simple app that checks availability of books in a store 
library = {
    'Books': {
        'Fiction': [('The Great Gatsby', 5), ('1984', 3)],
        'Non-fiction': [('Sapiens', 4), ('Educated', 2)]
    },
    'Members': {
        'John': {'Borrowed': ['The Great Gatsby'], 'MaxBorrowLimit': 3},
        'Sarah': {'Borrowed': [], 'MaxBorrowLimit': 3}
    }
}

# Check book availability
def check_availability(book_name):
    for category, books in library['Books'].items():
        for book, copies in books:
            if book == book_name and copies > 0:
                return True
    return False

# Borrow a book
def borrow_book(member_name, book_name):
    if not check_availability(book_name):
        print(f"Sorry, {book_name} is not available.")
        return

    if len(library['Members'][member_name]['Borrowed']) < library['Members'][member_name]['MaxBorrowLimit']:
        library['Members'][member_name]['Borrowed'].append(book_name)
        print(f"{member_name} successfully borrowed {book_name}.")
    else:
        print(f"{member_name} has reached the maximum borrowing limit.")

# Example usage
borrow_book('Sarah', 'Sapiens')

