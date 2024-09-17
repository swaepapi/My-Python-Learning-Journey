# Custom Functions 
#Calculating total price including tax

def total_price(price, tax_rate):
    return price + (price * tax_rate)

print(total_price(100, 0.08))  # 8% tax rate

# Conert temp from celsius to fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(25))

# Calculating the area of diffferent shapes 

def area_of_rectangle(length, width):
    return length * width

def area_of_circle(radius, pi=3.1416):
    return pi * (radius ** 2)

print(area_of_rectangle(5, 10))
print(area_of_circle(7))

# Returning multiple results
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([1, 3, 5, 7])
print(result)  

#Calculating Tips at arestaurant 
def calculate_tip(bill_amount, tip_percentage=15):
    return bill_amount * (tip_percentage / 100)

print(calculate_tip(50))  
