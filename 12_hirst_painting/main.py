import random
import colorgram
import turtle as t

veli = t.Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

veli.speed("fastest")
veli.penup()
veli.hideturtle()

veli.setheading(225)
veli.forward(300)
veli.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    veli.dot(20, random.choice(colors))
    veli.forward(50)

    if dot_count % 10 == 0:
        veli.setheading(90)
        veli.forward(50)
        veli.setheading(180)
        veli.forward(500)
        veli.setheading(0)




# colors = colorgram.extract('dots.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))

screen = t.Screen()
screen.exitonclick()