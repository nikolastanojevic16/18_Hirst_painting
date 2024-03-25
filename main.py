# import colorgram
import turtle
# colors = colorgram.extract('hirst_spot_painting.jfif', 15)

# rgb_colors = []

# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

from turtle import Turtle, Screen
import random
turtle.colormode(255)


color_list = [(198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120),
              (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158)]

t = Turtle()

t.hideturtle()
t.penup()
t.setheading(225)
t.forward(320)
t.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = Screen()
screen.exitonclick()
