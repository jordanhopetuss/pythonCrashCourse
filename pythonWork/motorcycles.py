# CHANGING, ADDING, and REMOVING ELEMENTS FROM A LIST
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modifying and replacing elemnts in a list
motorcycles[0] = 'ducati'
print(motorcycles)
# [ducati,yamaha,suzuki]

# Adding elemnts to a list with .append()
motorcycles.append("ducati")
print(motorcycles)
# [honda, yamaha, suzuki, ducati]

# Adding elements to a list and then add items to the list using a series of append() calls
motorcycle = []
motorcycle.append('honda')
motorcycle.append("yamaha")
motorcycle.append('suzuki')
print(motorcycle)

# Inserting methods into a list
dogs = ['labs', 'doodles', 'beagles']
dogs.insert(0, 'terriers')
dogs.insert(3, 'poodles')
print(dogs)

# Removing elements from a list

# del statement
del motorcycles[0]
print(motorcycles)

del dogs[3]
print(dogs)

# Removing items using the pop() method
# pop() method is used if you want to use the value from the list after removing it from a list.
# It removes the last item from that list and but it lets you work with the item after removing it.

poppedMotorcycles = motorcycles.pop()
print(motorcycles)
print(poppedMotorcycles)

lastOwned = motorcycles.pop()
print(f"The last motorcycle I owned was a {lastOwned.title()}. ")

firstOwned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {firstOwned.title()}. ")

# HOW TO DECIDE BTW .pop() METHOD AND del STATEMENT???
# Do I want to use the item as I remove it? Or, do I want to remove it from the list forever?

# Removing and item by VALUE
# For when you don't know the position of the value in the list
motorcycle.remove('honda')
print(motorcycle)

tooExpensive = 'suzuki'
motorcycles.remove(tooExpensive)
print(motorcycles)
print(f"A {tooExpensive.title()} is too expensive for me. ")
