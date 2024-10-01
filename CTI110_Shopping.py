# This program simulates shopping and displaying receipts

item1 = input(str("Enter the first item: "))
quantity1 = int(input(f"Enter the quantity of {item1}: "))
price1 = float(input(f"Enter the price of {item1}: "))

#Get info for item2
item2 = input(str("Enter the second item: "))
quantity2 = int(input(f"Enter the quantity of {item2}: "))
price2 = float(input(f"Enter the price of {item2}: "))

#Get info for item3
item3 = input(str("Enter the third item: "))
quantity3 = int(input(f"Enter the quantity of {item3}: "))
price3 = float(input(f"Enter the price of {item3}: "))

# Display top of the receipt
print()
print("Thanks for shopping at the Mann Co. Store!")
print("-" * 50)
print()
item = "ITEM"
quantity = "QUANTITY"
itemTotal = "ITEM TOTAL"
print(f"{item:<20}{quantity:<15}{itemTotal}")
print()
print(f"{item1:<20}{quantity1:<15}${price1 * quantity1:.2f}\n")
print(f"{item2:<20}{quantity2:<15}${price2 * quantity2:.2f}\n")
print(f"{item3:<20}{quantity3:<15}${price3 * quantity3:.2f}\n")
print()
print("-" * 50)
print()
#Calculate Subtotal
subtotal = float((price1 * quantity1) + (price2 * quantity2) + (price3 + quantity3))
print(f"Subtotal: {subtotal:.2f}")
print()
tax = float(subtotal * 0.07)
print(f"Sales Tax: {tax:.2f}")
print()
total = float(subtotal + tax)
print(f"Total Cost: {total:.2f}")
