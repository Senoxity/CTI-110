# Aiden Canady
# 11/12/24
# P4HW1_CanadyAiden
# Example for P4HW1

# Declare variables
enter_grades = int(input("How many grades will you enter? "))
module_grades = []
letter_grade = ""

# Collect grades from the user for each module
for i in range(enter_grades):
    inc = i + 1
    module_grades.append(float(input(f"Enter the grade for Module {inc}: ")))
    if module_grades[i] < 0 or module_grades[i] > 100:
        while module_grades[i] < 0 or module_grades[i] > 100:
            print("This program does not support numbers under 0 and over 100.")
            if module_grades[i] > 100:
                module_grades.remove(max(module_grades))
                module_grades.append(float(input(f"Enter the grade for Module {inc} again: ")))
            else:
                module_grades.remove(min(module_grades))
                module_grades.append(float(input(f"Enter the grade for Module {inc} again: ")))
      
# Display the lowest, highest, sum, and average of the grades
print()
print("Grades Summary:")
print("-" * 50)
print(f"Lowest grade: {min(module_grades)}")
print(f"Highest grade: {max(module_grades)}")
module_grades.remove(min(module_grades))
print(f"Modified List: {module_grades}")
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
