# defining function with main()

# important! variable "name" exist only in main function
def main():
    name = input("What's your name? ")
    hello(name)

# variable name doesn't exist in def finction.
# im puting variable name from main function, as parameter of function hello
# and using in print, parameter "to", from function hello.
# parameter "to" could be anythink   
def hello(to):
    print("Hello,", to)


# we are calling function main
main()