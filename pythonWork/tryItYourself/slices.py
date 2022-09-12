# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

myFoods = ['pizza', 'falafel', 'carrot cake',
           'cabbage rolls', 'sourdough bread', 'garden salad', 'cannoli', 'ice cream']
# Print the message 'The first three items in the list are: Then use a slice to print the first three items from that program's list.
print('The first three items in this list are: ')
print(myFoods[:3])
# The first three items in this list are:
# ['pizza', 'falafel', 'carrot cake']

# Print the message Three items from the middle of the list are:
print("Three items from the middle of the list are:")
print(myFoods[3:6])
# Three items from the middle of the list are:
# ['cabbage rolls', 'sourdough bread', 'garden salad']

print("The last three items in the list are: ")
print(myFoods[5:9])
# The last three items in the list are:
# ['garden salad', 'cannoli', 'ice cream']
