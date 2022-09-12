# Write a series of conditional tests. Print a statement describing each test and your prediction fro the results of each test. Your code should look something like this:

car = 'gmc'
car == 'gmc'
print('Is car == subaru? i predict true')
print(car == 'subaru')

print("\n Is car == 'audi'? I predict false. ")
print(car == 'audi')

print("\n Is car == 'oldsmobile'? I predict false. ")
print(car == 'oldsmobile')

print("\n Is car == 'gmc'? I predict true. ")
print(car == 'gmc')
# True
print(car.lower() == 'gmc')
# True
print(car.title() == 'gmc')
# False

# ------------------------------------------------

# Test for inequality and equality with strings
companyJingle = "Save big money and Menards. "
groceryJingle = "The natural way for caring for you. "

if companyJingle == groceryJingle:
    print("Do the businesses have copyright issues? ")
else:
    print("Commerical jingles are effective tools for brand awareness. ")

menu1 = "pasta bolognese"
menu2 = "pasta bolognese"

if menu1 == menu2:
    print("They have the same menu items this week at campus dining halls. ")
else:
    print("What on the menu this week chef? ")

# Test using the .lower() method
dogName = 'Shorty'
if dogName == 'shorty':
    print(True)
else:
    print(False)
# False

print(dogName == 'shorty')
# False
print(dogName.lower() == 'shorty')
# True

# Numerical tests involving equality and inequality, greater than and less than, greater than and equal to, and less than or equal to.
numList1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numList2 = [24, 5, 32, 15, 34, 89, 10, 91]

for number in numList2:
    if numList2 >= numList1:
        print(number)
    else:
        print("This number is NOT greater than or equal to the compared numbers")

# Tests using the keyword 'and' and the keyword 'or'.
if numList1 and numList2 == 56:
    print(numList1, numList2)
else:
    print(False)

# Test whether an item is in a list
for number in numList1:
    if number == numList1 or 24:
        print(number)
    else:
        print(False)

# Test whether and item is not in a list
number = 27
for numbers in numList2:
    if numbers == 27:
        print("27 is in this number list. ")
else:
    print('27 is not in this number list. ')
