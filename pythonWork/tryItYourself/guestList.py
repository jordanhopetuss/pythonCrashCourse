#  If you could invite anyone to a dinner party, living or dead, prnt a list to each person, inviiting them to dinner.

guestList = []

# del guestList[3]
# print(f"{guestList[3]} sorry you can no longer joing us! ")

guestList.append('tracie')
guestList.append('jordan')
guestList.append('alan')
guestList.append('faith')
guestList.append('joe')
guestList.append('kate')
guestList.append('maeve')
guestList.append('ezra')
guestList.append('ethan')

print(guestList)

inviteOne = guestList[0]
print(f"{inviteOne.title()} come over for dinner next Friday? ")

inviteTwo = guestList[1]
print(f"{inviteTwo.title()} come over for dinner next Friday? ")

inviteThree = guestList[2]
print(f"{inviteThree.title()} come over for dinner next Friday? ")

inviteFour = guestList[3]
print(f"{inviteFour.title()} come over for dinner next Friday? ")

inviteFive = guestList[4]
print(f"{inviteFive.title()} come over for dinner next Friday? ")

inviteSix = guestList[5]
print(f"{inviteSix.title()} come over for dinner next Friday? ")

inviteSeven = guestList[6]
print(f"{inviteSeven.title()} come over for dinner next Friday? ")

inviteEight = guestList[7]
print(f"{inviteEight.title()} come over for dinner next Friday? ")

inviteNine = guestList[8]
print(f"{inviteNine.title()} come over for dinner next Friday? ")

print(f"{inviteSeven.title()}, sorry you can't make it! ")


guestList.insert(6, 'ken')
guestList.pop(7)
print(guestList)

inviteSeven = guestList[6]
print(f"{inviteSeven.title()} come over for dinner next Friday? ")

print(f"{guestList}, we found a large table for Friday! ")

guestList.insert(5, 'alice')
guestList.insert(9, 'iris')
guestList.append('shorty')
print(guestList)

inviteTen = guestList[5]
inviteEleven = guestList[9]
inviteTwelve = guestList[11]


print(
    f"{inviteOne.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(f"{inviteTwo.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(f"{inviteThree.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(f"{inviteFour.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(f"{inviteFive.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(f"{inviteSix.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(f"{inviteSeven.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(f"{inviteEight.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(f"{inviteNine.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(f"{inviteTen.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(f"{inviteEleven.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(f"{inviteTwelve.title()} your invited to dinner this Friday! Click the link to RSVP, hope to see you there. ")
print(guestList)

# ---------------------------------------------------------- #

# Shrinking guest list
print(guestList)
# ['tracie', 'jordan', 'alan', 'faith', 'joe', 'alice', 'kate', 'ken', 'ezra', 'iris', 'ethan', 'shorty']
guestList.pop()
print(guestList.pop().title() +
      ", sorry I have to univite you to dinner. We don't have a table big enough! ")

guestList.pop()
print(guestList.pop().title() +
      ", sorry I have to univite you to dinner. We don't have a table big enough! ")
guestList.pop()
print(guestList.pop().title() +
      ", sorry I have to univite you to dinner. We don't have a table big enough! ")
guestList.pop()
print(guestList.pop().title() +
      ", sorry I have to univite you to dinner. We don't have a table big enough! ")
guestList.pop()
print(guestList.pop().title() +
      ", sorry I have to univite you to dinner. We don't have a table big enough! ")
guestList.pop()
print(guestList.pop().title() +
      ", sorry I have to univite you to dinner. We don't have a table big enough! ")

print(guestList)
print(len(guestList))
# guestZero = guestList.pop(0)
# print(f"{guestZero.title()}, you're invited for a dinner party this Friday! Click the link for more details. Hope to see you there! ")
# print(guestList)

# guestOne = guestList.pop(0)
# print(f"{guestOne.title()}, you're invited for a dinner party this Friday! Click the link for more details. Hope to see you there! ")
# print(guestList)

# guestTwo = guestList.pop(0)
# print(f"{guestTwo.title()}, you're invited for a dinner party this Friday! Click the link for more details. Hope to see you there! ")
# print(guestList)

# guestThree = guestList.pop(0)
# print(f"{guestThree.title()}, you're invited for a dinner party this Friday! Click the link for more details. Hope to see you there! ")
# print(guestList)

# guestFour = guestList.pop(0)
# print(f"{guestFour.title()}, you're invited for a dinner party this Friday! Click the link for more details. Hope to see you there! ")
# print(guestList)

# guestFive = guestList.pop(0)
# print(f"{guestFive.title()}, you're invited for a dinner party this Friday! Click the link for more details. Hope to see you there! ")
# print(guestList)

# guestSix = guestList.pop(0)
# print(f"{guestSix.title()}, you're invited for a dinner party this Friday! Click the link for more details. Hope to see you there! ")
# print(guestList)

# guestSeven = guestList.pop(0)
# print(f"{guestSeven.title()}, you're invited for a dinner party this Friday! Click the link for more details. Hope to see you there! ")
# print(guestList)

# guestEight = guestList.pop(0)
# print(f"{guestEight.title()}, you're invited for a dinner party this Friday! Click the link for more details. Hope to see you there! ")
# print(guestList)

# Call back error, popping from am empty list
# guestNine = guestList.pop(0)
# print(f"{guestNine.title()}, you're invited for a dinner party this Friday! Click the link for more details. Hope to see you there! ")
# print(guestList)
