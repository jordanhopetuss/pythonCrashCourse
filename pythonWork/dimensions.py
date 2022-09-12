# Tuples: allowing you to create a list of items that cannot change. Values that cannot change are immutable, and an immutable list is called a tuple.
# A tuple looks just like a list except you use paranthesis instead of square brackets. Once you define a tuple, you can access individual elements by using each item's index, just as you would for a list.

# Dimensions of a rectangle that always has a certain size
# Simple tuple
dimensions = (200, 50)
# Accessing data from dimensions at index [0]
print(dimensions[0])
print(dimensions[1])

# Tuples are technically defined by a comma but the paranthesis make the tuple look neater. If you want to define a tuple with one element, you need to include a trailing comma:
# myT = (3,) This can happen if tuples are generated automatically in a program.

# --------------------------------------------------------------------------------

# Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)

# Writing over a tuple: You can't modify a tuple, you CAN assign a new value to a variable that represents a tuple.
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

# Reassigned the variable dimensions with new values so it doesnt ring as a error in the system.
dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)
