# Aiden Canady
# 11/7/2024
# P4LAB1
# Program that utilizes turtle graphics

# Create Alex
import turtle          
win = turtle.Screen()  
alex = turtle.Turtle()

# Color and size options
alex.pensize(3)
alex.pencolor("red")
alex.shape("turtle")

# Draws a square
for i in range(4):
    alex.forward(50)
    alex.left(90)

# Move forward without drawing
alex.penup()
alex.forward(100)
alex.pendown()

# Draws a triangle
for i in range(3):
    alex.forward(80)
    alex.left(120)
