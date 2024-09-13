#FUNCTIONS

#Basic syntax
def greet():
    print("Hello Fidel, functions are fun!")

greet()

#Function parameters and Arguments 
def greet_me(name):
    print(f"Hello, {name}!")
    
greet_me("Fidel")

#Return Values
def addition(x, y):
    return x + y

result = addition(54, 20)
print(result)

#Default Parameters - can be used in no arguments are passed
def greet(name="Fidel Barasa"):
    print(f"Hello, {name}!")


greet()
greet("Fidel")

#Understanding functions Scope 
# Variables defined inside a function are local to that function and cannot be accessed outside of it 

def myfnct():
    age = 24
    print(age)

myfnct()
print(age) # This returns an error because the variable age cannot be accessed outside the function



