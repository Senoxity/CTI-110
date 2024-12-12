# Aiden Canady
# 10/17/24
# P2HW1
# A program that does some basic math on numbers that are entered. Formatting is used.

# Gather user input information (budget, expenses, etc.)
budget = float(input("Enter your travel budget: "))
destination = str(input("Enter your preferred destination: "))
gas = float(input("Approximately how much do you expect to spend on gas? "))
accom = float(input("Approximately how much do you expect to spend on hotels/accomodation? "))
food = float(input("Approximately how much do you expect to spend on food? "))

# Title graphic
print()
print()
print("----------Travel Expenses----------")

# Display output to user
print()
print(f"{'Budget:':<20}${budget:,.2f}\n")
print(f"{'Destination:':<20}{destination}\n")
print(f"{'Fuel:':<20}${gas:,.2f}\n")
print(f"{'Accomodations:':<20}${accom:,.2f}\n")
print(f"{'Food:':<20}${food:,.2f}\n")
print()
print("-" * 36)
print()

# Calculate remaining money from budget
remainder = budget - gas - accom - food
print(f"{'Remaining Balance:':<20}${remainder:,.2f}\n")
