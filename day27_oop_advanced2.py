# Multiple inheritance - allows a class to inherit from more than one parent class.

# Parent class 1
class Animal:
    def speak(self):
        return "Animal sound"

# Parent class 2
class Bird:
    def fly(self):
        return "I can fly"

# Child class inheriting from both Animal and Bird
class Parrot(Animal, Bird):
    def talk(self):
        return "I can talk!"

# Creating an object of the child class
parrot = Parrot()

# Accessing methods from both parent classes
print(parrot.speak())  # Inherited from Animal
print(parrot.fly())    # Inherited from Bird
print(parrot.talk())   # Defined in Parrot


# Abstract Base Classes (ABC) - help define a common interface for subclasses

from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

# Subclass implementing the abstract methods
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
    def stop_engine(self):
        return "Car engine stopped"

# Subclass implementing the abstract methods
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
    
    def stop_engine(self):
        return "Motorcycle engine stopped"

# Instantiating objects of the subclasses
car = Car()
motorcycle = Motorcycle()

print(car.start_engine())       # Output: Car engine started
print(motorcycle.start_engine()) # Output: Motorcycle engine started


# Method Resolution Order (MRO): determines the order in which methods are inherited in case of multiple inheritance.

class A:
    def process(self):
        return "Method from class A"

class B(A):
    def process(self):
        return "Method from class B"

class C(A):
    def process(self):
        return "Method from class C"

class D(B, C):
    pass

# Creating an object of class D
d = D()

# Calling the process method
print(d.process())  # Output: Method from class B

# Viewing the MRO of class D
print(D.mro())  


