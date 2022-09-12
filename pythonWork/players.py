# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Pulling from index 0 = charles : = through 3 = michael
print(players[0:3])
# [charles, martina, michael]

# If you omit the first index in a slice, Python starts the slice at the begining of the list
print(players[:4])
# [charles, martina, michael, florence]

print(players[2:])
# ['michael', 'florence', 'eli']

print(players[-3:])
# ['michael', 'florence', 'eli']

# There can be a third item in the slicing brackets. This third value tells python how many items to skip in the specified range.
print(players[1:3:2])
# ['martina']

# -------------------------------------------------------
# Looping through slices

print("Here's the first three players on my team: ")
for player in players[:3]:
    print(player.title())

# Here's the first three players on my team:
# Charles
# Martina
# Michael

# --------------------------------------------------------
# Copying a list with slicing
# [:] tells python to make a slice that starts at the first item and ends with the last item, producin a copy of the entire list.
