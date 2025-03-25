import turtle
import datetime
import math
import random

turtle.setup(500, 500)
turtle.bgcolor("black")
turtle.tracer(0)

CLOCK_RADIUS = 100
NUM_STARS = 50

def is_outside_circle(x, y, radius):
    return math.sqrt(x ** 2 + y ** 2) > radius + 10

stars = []
for _ in range(NUM_STARS):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.speed(0)

    while True:
        x, y = random.randint(-200, 200), random.randint(-200, 200)
        if is_outside_circle(x, y, CLOCK_RADIUS):
            star.goto(x, y)
            break

    stars.append(star)

def twinkle_stars():
    for star in stars:
        star.clear()
        while True:
            x, y = random.randint(-200, 200), random.randint(-200, 200)
            if is_outside_circle(x, y, CLOCK_RADIUS):
                star.goto(x, y)
                break
        star.dot(random.randint(2, 5), "white")

    turtle.update()
    turtle.ontimer(twinkle_stars, 500)

class ClockFace:
    def __init__(self, radius=CLOCK_RADIUS):
        self.radius = radius

    def draw(self):
        turtle.penup()
        turtle.goto(0, -self.radius)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.circle(self.radius)

        for i in range(12):
            angle = 90 - i * 30
            x = self.radius * 0.85 * math.cos(math.radians(angle))
            y = self.radius * 0.85 * math.sin(math.radians(angle))
            turtle.penup()
            turtle.goto(x, y - 5)
            turtle.pendown()
            turtle.pencolor("white")
            turtle.write(i if i != 0 else 12, align="center", font=("Arial", 12, "bold"))

        for i in range(60):
            angle = 90 - i * 6
            x1 = self.radius * 0.95 * math.cos(math.radians(angle))
            y1 = self.radius * 0.95 * math.sin(math.radians(angle))
            x2 = self.radius * math.cos(math.radians(angle))
            y2 = self.radius * math.sin(math.radians(angle))
            turtle.penup()
            turtle.goto(x1, y1)
            turtle.pendown()
            if i % 5 == 0:
                turtle.pensize(2)
            else:
                turtle.pensize(1)
            turtle.goto(x2, y2)
class Hand:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color
        self.hand_turtle = turtle.Turtle()
        self.hand_turtle.hideturtle()
        self.hand_turtle.speed(0)
        self.hand_turtle.pensize(self.width)
        self.hand_turtle.pencolor(self.color)

    def draw(self, angle):
        self.hand_turtle.clear()
        self.hand_turtle.penup()
        self.hand_turtle.goto(0, 0)
        self.hand_turtle.setheading(90 - angle)
        self.hand_turtle.pendown()
        self.hand_turtle.forward(self.length)

class AnalogWatch:
    def __init__(self):
        self.face = ClockFace()
        self.hour_hand = Hand(50, 4, "white")
        self.minute_hand = Hand(70, 3, "cyan")
        self.second_hand = Hand(90, 2, "red")

    def draw_face(self):
        self.face.draw()

    def update_time(self):
        now = datetime.datetime.now()
        hour_angle = (now.hour % 12) * 30 + now.minute * 0.5
        minute_angle = now.minute * 6 + now.second * 0.1
        second_angle = now.second * 6

        self.hour_hand.draw(hour_angle)
        self.minute_hand.draw(minute_angle)
        self.second_hand.draw(second_angle)

        turtle.update()
        turtle.ontimer(self.update_time, 50)

class DigitalWatch:
    def __init__(self, format_24=True):
        self.format_24 = format_24
        self.text_turtle = turtle.Turtle()
        self.text_turtle.hideturtle()
        self.text_turtle.speed(0)

    def update_time(self):
        self.text_turtle.clear()
        self.text_turtle.penup()
        self.text_turtle.goto(0, -130)
        self.text_turtle.pencolor("white")
        self.text_turtle.pendown()
        now = datetime.datetime.now()
        time_str = now.strftime("%H:%M:%S") if self.format_24 else now.strftime("%I:%M:%S %p")
        self.text_turtle.write(time_str, align="center", font=("Arial", 16, "bold"))

        turtle.update()
        turtle.ontimer(self.update_time, 500)

if __name__ == "__main__":
    analog = AnalogWatch()
    digital = DigitalWatch(format_24=True)

    analog.draw_face()
    analog.update_time()
    digital.update_time()

    twinkle_stars()

    turtle.done()
