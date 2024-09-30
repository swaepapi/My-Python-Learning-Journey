# Creating Classes and Objects
# Defining a class called 'Car'
class Car:
    # Constructor method: initializes the attributes of the class
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # A method to describe the car
    def describe_car(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing the method
print(my_car.describe_car())

# Encapsulation

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # private attribute

    # Public method to get the account balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance is {self.__balance}"
        else:
            return "Invalid deposit amount."

# Creating an instance of BankAccount
my_account = BankAccount("Fidel", 1000)

# Accessing public method
print(my_account.get_balance())  # Output: 1000

# Depositing money
print(my_account.deposit(500))  # Output: Deposited 500. New balance is 1500


# Class Methods vs. Instance Methods

class Dog:
    species = "Canine"  # Class attribute, shared by all instances

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Class method
    @classmethod
    def get_species(cls):
        return f"All dogs are {cls.species}."

# Creating an instance of Dog
dog = Dog("Buddy", 3)

# Accessing instance method
print(dog.description())  # Output: Buddy is 3 years old.

# Accessing class method
print(Dog.get_species())  # Output: All dogs are Canine.


