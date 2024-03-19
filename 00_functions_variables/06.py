# defining my own function

# "to" is parameter. "world" is default if no parameters
def hello(to="world"):
    print("Hello, ", to)

# using defined function, without parameters (using default)
hello()

name = input("What's your name? ")

# here we declare, that function "hello", should use parameter "name"
hello(name)