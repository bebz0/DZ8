import turtle
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


class Watch:
    def update_time(self):
        pass


class AnalogWatch(Watch):
    def init(self):
        super().__init__()
        self.face = ClockFace()
        self.hour_hand = Hand(50, 4, "black")
        self.minute_hand = Hand(70, 3, "blue")
        self.second_hand = Hand(90, 2, "red")

    def update_time(self):
        turtle.tracer(0)
        turtle.clear()
        self.face.draw()
        now = datetime.datetime.now()
        self.hour_hand.draw((now.hour % 12) * 30 + now.minute * 0.5)
        self.minute_hand.draw(now.minute * 6)
        self.second_hand.draw(now.second * 6)
        turtle.update()
        turtle.ontimer(self.update_time, 1000)


class DigitalWatch(Watch):

    def __init__(self, format_24=True):
        super().__init__()
        self.format_24 = format_24

    def update_time(self):
        turtle.tracer(0)
        turtle.penup()
        turtle.goto(0, -130)
        turtle.pendown()
        now = datetime.datetime.now()
        if not self.format_24:
            time_str = now.strftime("%I:%M:%S %p")
        else:
            time_str = now.strftime("%H:%M:%S")
        turtle.write(time_str, align="center", font=("Arial", 16, "bold"))
        turtle.update()
        turtle.ontimer(self.update_time, 1000)


if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()
    analog = AnalogWatch()
    digital = DigitalWatch(format_24=True)
    analog.update_time()
    digital.update_time()
    turtle.done()