# Choose a version of foods.py and write two for loops to print each list of foods.

# Adding more pizzas to the list and printing out the list of pizzas to the terminal.
pizzas = ["pepperoni", "veggie lovers", "caprice", "cheese"]

pizzas.append('meat lovers')

for pizza in pizzas:
    print(pizza)

# Making all the types of pizza .upper() when printing out the foods list.
myFoods = ['pizza', 'falafel', 'carrot cake',
           'cabbage rolls', 'sourdough bread', 'garden salad']
print('\n')

for food in myFoods:
    print(food.title())
    print(food.upper())
