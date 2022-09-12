# Start with your program from Exercise 4.1 Make a copy of the list of pizzas, and call it friendPizzas.
pizzas = ["pepperoni", "veggie lovers", "caprice", "cheese"]
friendPizzas = pizzas[:]

# Add a new pizza to the original pizzas list
pizzas.append("meat lovers")
print(pizzas)
# ['pepperoni', 'veggie lovers', 'caprice', 'cheese', 'meat lovers']

# Add a new pizza to the friendPizzas list
friendPizzas.append("anchovy")
print(friendPizzas)
# ['pepperoni', 'veggie lovers', 'caprice', 'cheese', 'anchovy']

print('\n')
print("My favorite pizzas are: ")
print(pizzas)
print("\nMy friend's favorite pizzas are: ")
print(friendPizzas)
print("\n")
