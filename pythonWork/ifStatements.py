
# List from cars.py file
cars = ['bmw', 'audi', 'toyota', 'subaru']
# Need to be printed in the title() case
# Except, BMW is in all upper() case

# For loop
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional tests
# At the heart of every if statement is an expression TRUE or FALSE
# Checking for equality: car = 'bmw | car == 'bmw' | True

# Example 2: car = 'audi' | car == 'bmw' | False

# Ignoring case when checking for equality
# CHECKING FOR EQUALITY IS CASE SENSITIVE IN PYTHON

# Example: car = 'Audi' | car == 'audi' | False

# If case sensitivity isn't a factor and you want to check teh value of the variable. use the .upper(), .lower(), .title() methods

# Example: car = "Audi" | car.lower() == "audi" | True

car = 'Audi'
car.lower() == 'audi'
print(car)
