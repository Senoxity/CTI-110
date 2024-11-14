# P3HW2- Salary Calculator
# Aiden Canady
# request employee information

numEmploy = 0
totalOvertime = 0.0
totalReg = 0.0
totalGross = 0.0
name = input("Enter employee's name or 'Done' to terminate: ")

while name.lower() != "done":
    hoursWorked = float(input(f"Enter number of hours {name} worked: "))

    payRate = float(input(f"Enter {name}'s pay rate: "))

    #evalute overtime

    if hoursWorked >40 :

        #calculate overtime
        overtimeHours = hoursWorked - 40
        #Calculate overPay
        overPay = overtimeHours * (payRate * 1.5)

        #calculate salary for reg hours

        regPay = 40 * payRate

        # calculate gross pay

        grossPay = regPay + overPay
    else:

        overPay = 0
        overtimeHours = 0

        regPay = hoursWorked * payRate
        grossPay = regPay

    numEmploy += 1
    totalOvertime += overPay
    totalReg += regPay
    totalGross += grossPay

    # Display output

    print("-------------------------------------")
    print("Employee name:  ",name,"\n")

    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
    print('--------------------------------------------------------------------------------------------------')
    print(f'{hoursWorked:<15}{payRate:<12}{overtimeHours:<12}{overPay:<20}{"$"}{regPay:<20.2f}{"$"}{grossPay:.2f}')
    print()
    name = input("Enter employee's name or 'Done' to terminate: ")

print()
print(f"Total number of employees entered: {numEmploy}")
print(f"Total amount of overtime paid: ${totalOvertime:.2f}")
print(f"Total amount paid for regular hours: ${totalReg:.2f}")
print(f"Total amount paid in gross: ${totalGross:.2f}")


    
