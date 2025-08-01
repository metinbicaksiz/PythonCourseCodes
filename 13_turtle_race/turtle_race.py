from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Choose a color", "Choose a color:")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                is_race_on = False
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        step = random.randint(0, 10)
        turtle.forward(step)


screen.exitonclick()