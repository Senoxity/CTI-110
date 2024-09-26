# Aiden Canady
# 9/26/24
# P1HW2
# A program that does some basic math on numbers that are entered.

# Gather user input information (budget, expenses, etc.)
budget = int(input("Enter your travel budget: "))
destination = str(input("Enter your preferred destination: "))
gas = int(input("Approximately how much do you expect to spend on gas? "))
accom = int(input("Approximately how much do you expect to spend on hotels/accomodation? "))
food =int(input("Approximately how much do you expect to spend on food? "))

# Title graphic
print()
print()
print("----------Travel Expenses----------")

# Display output to user
print("Destination: ", destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", accom)
print("Food: ", food)
print()

# Calculate remaining money from budget
remainder = budget - gas - accom - food
print("Remaining Balance: ", remainder)
