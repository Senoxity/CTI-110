# Aiden Canady
# 10/24/2024
# P3LAB
# Calculates money based on an entered value

# Declare variables
amount = float(input("Enter an amount of money: $"))
cents = int(round(amount * 100))

# Calculate money
dollars = cents // 100
cents -= dollars * 100
quarters = cents // 25
cents -= quarters * 25
dimes = cents // 10
cents -= dimes * 10
nickels = cents // 5
cents -= nickels * 5
pennies = cents

# Display the result, adjusting for singular and plural forms
if dollars == 1:
    print(f"1 dollar")
elif dollars > 1:
    print(f"{dollars} dollars")

if quarters == 1:
    print(f"1 quarter")
elif quarters > 1:
    print(f"{quarters} quarters")

if dimes == 1:
    print(f"1 dime")
elif dimes > 1:
    print(f"{dimes} dimes")

if nickels == 1:
    print(f"1 nickel")
elif nickels > 1:
    print(f"{nickels} nickels")

if pennies == 1:
    print(f"1 penny")
elif pennies > 1:
    print(f"{pennies} pennies")
