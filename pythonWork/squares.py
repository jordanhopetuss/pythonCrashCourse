# squares = []
# for values in range(1, 11):
#     squares.append(values ** 2)
# print(squares)

# Simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehension
squares = []
squares = [value ** 2 for value in range(1, 11)]
print(squares)
