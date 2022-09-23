# If statemenst continued...
# Does not equal != and if statements
requestedToppings = []
# if requestedToppings != 'anchovies':
#     print('Hold the anchovies! ')
# if 'mushrooms' in requestedToppings:
#     print('Adding mushrooms')
# if 'extra cheese' in requestedToppings:
#     print('Adding extra cheese')
# if 'pepperoni' in requestedToppings:
#     print('Adding peperoni')

# print("\nFinished making your pizza! ")

# --------------------------------------------
# Adding in a for loop to check for a special item in a list
if requestedToppings:
    for requestedTopping in requestedToppings:
        print("Adding " + requestedTopping + ".")
    print("\nFinished making your pizza! ")
else:
    print("Are you sure you want a plain pizza? ")

# Numberical comparison
# age = 18
# age == 18
# True

# -------- Using Multiple Lists --------------
availableToppings = ["mushrooms", "olives",
                     "green peppers", "onions", "pepperoni", "extra cheese"]

requestedToppings = ["mushrooms", "french fries",
                     "jalapenos", "pickles", "pineapple", "canadian bacon", "extra cheese"]
for requestedTopping in requestedToppings:
    if requestedTopping in availableToppings:
        print(f"Adding {requestedTopping} to your pizza. ")
    else:
        print(f"Sorry, we do not have {requestedTopping}. ")
print("\nFinished making your pizza! ")
