# Think of something you could store in a list. Write a program that creates a list containing these items and then uses each function introduced in the chapter atleast once.

mountainRanges = ['rocky', 'appalachian', 'olympic', 'smokey']

# .sort() method - prints items alphabetically
mountainRanges.sort()
print(mountainRanges)
# len() function
print(len(mountainRanges))
# .reverse() method
mountainRanges.reverse()
print(mountainRanges)
# sorted() function
sorted(mountainRanges)
print(mountainRanges)
# .remove() method
mountainRanges.remove('smokey')
print(mountainRanges)
# .pop() method
mountainRanges.pop(2)
print(mountainRanges)

# .insert() method
mountainRanges.insert(0, 'smokey')
print(mountainRanges)

mountainRanges.insert(2, 'galapagos')
print(mountainRanges)
# .append() method

mountainRanges.append('bruneau dunes')
print(mountainRanges)

# del statement
del mountainRanges[4]
print(mountainRanges)

# Modify elements by mountainRanges[insert index] = 'new item being replaced to the list'
mountainRanges[2] = 'bruneau dunes'
print(mountainRanges)

del mountainRanges[2]
print(mountainRanges)
