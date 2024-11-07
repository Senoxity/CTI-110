# Aiden Canady
# 11/7/2024
# P4LAB2
# Displays multiplication tables

# Obtain user input
num = int(input("Enter an integer: "))
run = "yes"
if num < 0:
    print("This program does not support negative numbers.")
# Calculate times tables
else:
    while run.lower() != "no":
        for i in range(13):
            total = num * i
            print(f"{num} * {i} = {total}")
        run = input("Do you want to run the program again? ")
        

    
