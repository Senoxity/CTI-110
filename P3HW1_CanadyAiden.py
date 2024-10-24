# Aiden Canady
# 10/20/2024
# P2HW2
# Program that stores grades in a list

# Declare variables
module_grades = []
letter_grade = ""

# Collect grades from the user for each module
module_grades.append(float(input("Enter the grade for Module 1: ")))
module_grades.append(float(input("Enter the grade for Module 2: ")))
module_grades.append(float(input("Enter the grade for Module 3: ")))
module_grades.append(float(input("Enter the grade for Module 4: ")))
module_grades.append(float(input("Enter the grade for Module 5: ")))
module_grades.append(float(input("Enter the grade for Module 6: ")))

# Display the lowest, highest, sum, and average of the grades
print()
print("Grades Summary:")
print("-" * 50)
print(f"Lowest grade: {min(module_grades)}")
print(f"Highest grade: {max(module_grades)}")
print(f"Sum of grades: {sum(module_grades)}")
average = sum(module_grades) / len(module_grades)
print(f"Average of grades: {average:.2f}")
print("-" * 50)

if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print()
print(f"Your average letter grade is {letter_grade}.")
'''
PSUEDOCODE

Declare list module_grades

Append float input "Enter the grade for Module 1: "
Append float input "Enter the grade for Module 2: "
Append float input "Enter the grade for Module 3: "
Append float input "Enter the grade for Module 4: "
Append float input "Enter the grade for Module 5: "
Append float input "Enter the grade for Module 6: "

Display 25 dashes
Display "Grades Summary:"
Display Lowest Grade (min(module_grades))
Display Highest Grade (max(module_grades))
Display Sum of all Grades (sum(module_grades))
Display Average Grade (sum / len)
'''

