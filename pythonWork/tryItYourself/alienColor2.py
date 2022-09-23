# If-else chain practice
alienColor = ["green", "yellow", "red"]

if alienColor == "green":
    print("5 points! ")
elif alienColor != "green":
    print("Earn 10 points! ")
else:
    print("Find the next alien in area 51. ")
# Earn 10 points!

if "green" in alienColor:
    print("Earn 5 points! ")
elif "red" in alienColor:
    print("Earn 10 points! ")
# Earn 5 points!
