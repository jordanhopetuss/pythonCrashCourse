firstName = "ada"
lastName = "lovelace"
# Using variables in f-strings with f = format "{}{}"
fullName = f"{firstName}{lastName}"
print(fullName)
# f-string example in a print statement with method inserted
print(f'Hello, {fullName.title()}! ')

#  -------------------------------------- #

# Adding white spaces w/ tabs or new lines

print("Python")
# Insert a tab \t
print("\tPython")
#  Insert a newline \n
print("Languages:\nPython\nC\nJavascript")
#  Combining tabs and newlines
print("Languages:\n\tPython\n\tC\n\tJavascript")

# --------------------------------- #
# Stripping whitespaces from data
favoriteLanguage = " Python "
# Removes white space on the right -or- left -or- both sides of values
print(favoriteLanguage.rstrip())
print(favoriteLanguage.lstrip())
print(favoriteLanguage.strip())
# Used to clean up user inputbefore values are stored in a program
