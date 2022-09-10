# Practice: Store the location of 5 places in the world you'd like to visit.
vacation = ['belize', 'portugal', 'new foundland',
            'costa rica', 'us virgin islands']
# Store the location in a list
# Use sorted() to print your list in alphabetical order
print(vacation)
print(sorted(vacation))
# Use sorted() to print your list in reverse
vacation.reverse()
print(vacation)
# Show that your list is still in original order by printing it again - REVERSE METHOD CHANGES A LIST PERMANANTLY UNLESS REVERSED BACK AGAIN
vacation.reverse()
print(vacation)
# Use reverse() to change the order of your list again. Print the list to show that its order has been changed.
vacation.reverse()
print(vacation)
# User reverse() again to show the list in original order
vacation.reverse()
print(vacation)
# use sort() method to change your list so it's stored alphabetically print both lists to show the order has been changed.
vacation.sort()
print(vacation)
# Use sort() to change your list so it's stored in reverse alphabetical order. Print the lists to show that the order has changed.
vacation.sort(reverse=True)
print(vacation)
vacation.sort(reverse=False)
print(vacation)
