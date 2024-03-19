# float variables

x = float(input("Number one: "))
y = float(input("Number two: "))

z = round(x + y)

# round function and puting "," every "000"
print(f"{z:,}")

# dividing and rounding result
div = round(x / y, 2)
print(f"One version of rounding: {div}")

# or

div2 = x / y
print(f"Second version of rounding: {div2:.2f}")