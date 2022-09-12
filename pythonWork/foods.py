# Copying a list with slicing
# [:] tells python to make a slice that starts at the first item and ends with the last item, producin a copy of the entire list.

myFoods = ['pizza', 'falafel', 'carrot cake',
           'cabbage rolls', 'sourdough bread', 'garden salad']

friendFoods = myFoods[:]
print("My favorite foods are: ")
print(myFoods)
# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cabbage rolls', 'sourdough bread', 'garden salad']

print("\nMy friend's favorite foods are: ")
print(friendFoods)
# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cabbage rolls', 'sourdough bread', 'garden salad']

# To showcase each list was saved seperately we add a new item to the end of each list using .append() method
myFoods.append('cannoli')
friendFoods.append('ice cream')
print(myFoods)
# ['pizza', 'falafel', 'carrot cake', 'cabbage rolls', 'sourdough bread', 'garden salad', 'cannoli']
print(friendFoods)
# ['pizza', 'falafel', 'carrot cake', 'cabbage rolls', 'sourdough bread', 'garden salad', 'ice cream']
