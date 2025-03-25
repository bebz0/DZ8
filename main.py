import turtle
import time
import datetime
import math


class Digit:

    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.write(self.number, align="center", font=("Arial", 12, "bold"))

    class ClockFace:
        def init(self, radius=100):
            self.radius = radius

        def draw(self):
            turtle.penup()
            turtle.goto(0, -self.radius)
            turtle.pendown()
            turtle.circle(self.radius)
            for i in range(1, 13):
                angle = i * 30
                x = self.radius * 0.85 * math.cos(angle * 3.14159 / 180)
                y = self.radius * 0.85 * math.sin(angle * 3.14159 / 180)
                Digit(x, y, i).draw()


class Hand:

    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def draw(self, angle):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(angle)
        turtle.pendown()
        turtle.pensize(self.width)
        turtle.pencolor(self.color)
        turtle.forward(self.length)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
