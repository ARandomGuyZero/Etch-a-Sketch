"""
Etch-a-Sketch
Author: Alan
Date: September 6th 2024

This script generates an Etch-a-Sketch game, where the player can move a turtle using the W/A/S/D keys to draw
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    """
    Moves the arrow forwards
    """
    tim.forward(10)

def move_backwards():
    """
    Moves the arrow backwards
    """
    tim.backward(10)

def counter_clockwise():
    """
    Moves the arrow counter-clockwise
    """
    tim.right(5)
    tim.heading()

def clockwise():
    """
    Moves the arrow clockwise
    """
    tim.right(5)
    tim.heading()

def clear():
    """
    Clears the screen and returns the arrow to the base position
    """
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards) # Press w to move forwards
screen.onkeypress(key="s", fun=move_backwards) # Press s to move backwards
screen.onkeypress(key="a", fun=counter_clockwise) # Press a to move counter-clockwise
screen.onkeypress(key="d", fun=clockwise) # Press d to move clockwise
screen.onkeypress(key="c", fun=clear) # Press c to clear the screen
screen.exitonclick()
