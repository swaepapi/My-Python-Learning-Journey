# Generators - Generators are a simple way to create iterators in Python
# Instead of returning a value and ending, a generator yields multiple values one at a time, which is useful for handling large datasets efficiently.

# Creating a Generator Using yield
def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count  # yield the current count and pause execution
        count += 1   # increment count and continue on next iteration

# Using the generator
for number in count_up_to(5):
    print(number)


# Generator Expressions
# List comprehension (creates a full list in memory)
squares_list = [x**2 for x in range(5)]

# Generator expression (creates a generator, not a list)
squares_gen = (x**2 for x in range(5))

# You can iterate over it or use next()
for square in squares_gen:
    print(square)


# Fibonacci Sequence Using Generators
def fibonacci():
    a, b = 0, 1
    while True:
        yield a  # yield must be inside a function
        a, b = b, a + b

# Use the generator to get the first 10 Fibonacci numbers
fib_gen = fibonacci()

for _ in range(10):
    print(next(fib_gen))



# Use Case: File Reading with Generators

def read_large_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()  # yield one line at a time

# Using the generator to process the file line by line
for line in read_large_file('example.txt'):
    print(line)
