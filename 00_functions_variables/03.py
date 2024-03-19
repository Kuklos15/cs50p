# string methods

#name = input("What's your name? ")


# remove whitespace from string
#name = name.strip()

# capitalize user's name - only first letter
#name = name.capitalize()

# capitalize user's name - first and another word
#name = name.title()

# we can use more function in one line
# and even use this function in one line with input and assinging variables
name = input("What's your name? ").strip().title()

print(f"Hello, {name}")

# we can split string by using function split()
first, last = name.split(" ")
print (f"Your first name: {first}")
print (f"Your last name {last}")