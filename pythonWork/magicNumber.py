# Test to see if two numbers are not equal
answer = 17

if answer != 42:
    print("That's not the correct answer, try again!")

# Checking multiple conditions
age0 = 22
age1 = 18
# if age0 >= age1 and age1 >= 21:
#     print("True")
# else:
#     print("False")

# Use paranthesis around individual tests to improve readability
if (age0 >= 21) and (age1 >= 21):
    print("22 is greater than 21, but 18 is less than 21. ")
else:
    print(False)
