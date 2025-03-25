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