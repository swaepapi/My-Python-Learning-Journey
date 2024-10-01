# Attributes and Methods

class Car:
    # Class attribute (same for all instances)
    wheels = 4
    
    def __init__(self, brand, model):
        # Instance attributes (unique for each instance)
        self.brand = brand
        self.model = model
    
    # Instance method
    def car_info(self):
        return f"This car is a {self.brand} {self.model}."

# Create instances of Car
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing instance and class attributes
print(car1.car_info())   # Output: This car is a Toyota Corolla.
print(car2.car_info())   # Output: This car is a Honda Civic.

# Accessing class attribute
print(f"Both cars have {car1.wheels} wheels.")  # Output: Both cars have 4 wheels.


# Inheritance

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Another child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Creating instances
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy barks.
print(cat.speak())  # Output: Whiskers meows.

# Polymorphism

class Bird:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} chirps."

class Fish:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} does not make sound."

# Function that demonstrates polymorphism
def animal_sound(animal):
    print(animal.speak())

# Using polymorphism
sparrow = Bird("Sparrow")
goldfish = Fish("Goldfish")

animal_sound(sparrow)   
animal_sound(goldfish)  

