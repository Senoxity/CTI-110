# Aiden Canady
# 10/8/2024
# P2LAB1
# Program that calculates parts of a circle based on a given radius

# Import libraries
import math

# Declare variables
radius = float(input("Enter a radius of a circle: "))

# Complete calculations
diameter = radius * 2
circum = (radius * 2) * math.pi
area = math.pow(radius, 2) * math.pi

# Display values back to user
print()
print("-" * 50)
print(f"The diameter of the circle is {diameter:.1f}\n")
print(f"The circumference of the circle is {circum:.2f}\n")
print(f"The area of the circle is {area:.3f}\n")
print("-" * 50)
