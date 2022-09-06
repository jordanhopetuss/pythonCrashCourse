# Learning python lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Printing out individual items in a list without brackets
# Calling the first item in the bicycles index = trek
# Indexing starts at 0 with lists not 1!!!
print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

# Negaticve indexing pulls from the end of a list no matter how long it is! -1 returns the last item in a list, -2 returns the second to last item in a list, etc.
print(bicycles[-1])
print(bicycles[-2])

# Using individual values from a list like any other variable
message = f"My first bicycle was a {bicycles[1].title()}. "
print(message)
