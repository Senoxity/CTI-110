# Aiden Canady
# 9/24/24
# P1HW1
# Get integer input from the user and perfrom math calculations

# Title Graphic
print("-----Calculating Exponents-----")
print()
print()

# Get info from user
baseValue = int(input("Enter the integer as the base value: "))
exponent = int(input("Enter the integer as the exponent: "))
print()
print()

# Calculate the value of the exponent
solution = baseValue ** exponent
print(baseValue, "raised to the power of", exponent, "is equal to", solution, "!!")

print()
print()
# Title Graphic
print("-----Addition & Subtraction-----")
print()
print()

# Obtain user input
startInt = int(input("Enter a starting integer: "))
addInt = int(input("Enter an integer to add: "))
subtractInt = int(input("Enter an integer to subtract: "))
print()
print()

# Calculate result
addSolution = startInt + addInt - subtractInt
print(startInt, "+", addInt, "-", subtractInt, "is equal to", addSolution)
