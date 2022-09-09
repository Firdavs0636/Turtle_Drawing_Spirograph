import random
import turtle as t

downy = t.Turtle()
downy.speed(11)
t.colormode(255)
current_heading = downy.heading()
downy.setheading(current_heading + 10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph (size_of_gap):
    for _ in range(int(360/size_of_gap)):
        downy.circle(100)
        downy.color(random_color())
        downy.setheading(downy.heading() + size_of_gap)


draw_spirograph(2)
screen = t.Screen()
screen.exitonclick()