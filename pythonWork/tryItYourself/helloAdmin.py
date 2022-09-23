# Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:

usernames = ["admin", "Jordan", "Stacy", "Polly",
             "Sully", "Shorty", "Akamaru", "Gypsy"]
# If the user name is 'admin' print a special greeting such as Hello admin, would you liek to see a status report?
for username in usernames:
    if username == 'admin':
        print(
            f"Hello {username}, would you like to see a status report? ")
# Otherwise print a generic greeting like thank you for logging in again.
    else:
        print("Please create a username. ")
