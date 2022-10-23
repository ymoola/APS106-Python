# APS106 Lab 1 - Drawing Shapes with Turtle
# Student Name: Yusuf Moola
# PRA Section: 0101


################################################
# Part 2 - Draw your initials
################################################

# provide access to the Turtle module
import turtle

# bring the turtle to life and call it alex
alex = turtle.Turtle()


# use alex to draw your first and last initials
# TODO: WRITE YOUR CODE HERE

alex.pensize(8) 
alex.penup()
alex.fd(110)
alex.pendown()
alex.right(110)
alex.fd(150)
alex.bk(65)
alex.right(125)
alex.fd(80)
alex.right(140)

alex.pensize(8)
alex.penup()
alex.fd(120)
alex.pendown()
alex.right(90)
alex.fd(150)
alex.bk(150)
alex.left(45)
alex.fd(90)
alex.left(95)
alex.fd(90)
alex.right(140)
alex.fd(150)


turtle.done()
