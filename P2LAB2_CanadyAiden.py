# Aiden Canady
# 10/10/2024
# P2LAB2
# Returns gas mileage info via dictionaries

# Declare variables
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}
keys = cars.keys()


# Obtain user input
print(keys)
answer = input("Enter a vehicle to see it's mpg: ")
print(f"The {answer} gets {cars[answer]} miles per gallon.")
miles = int(input(f"How many miles will you drive the {answer}? "))

# Calculate gallons of gas
trip = cars[answer] / miles
print(f"Approximately {trip:.2f} gallon(s) of gas are needed to drive the {answer} {miles} miles.")
