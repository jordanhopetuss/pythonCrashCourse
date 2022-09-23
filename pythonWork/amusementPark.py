# if-elif-else statements syntax
# Charging different rates for different age groups
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age > 65:
    price = 20

print(f"Your admissions cost is ${price}. ")

# -----------------------------------------

# Ommitting the else block means every block of code must pass the specific test to be executed.
# Else is a catchall statement
