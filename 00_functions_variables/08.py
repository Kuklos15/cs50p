# return

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

# we are defining our own function
def square(n):
    # without return, couldn't use the value in main function
    return n * n



main()