import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinate = [-120, -70, -20, 30, 80, 130]
all_turtles = []

for turtle_index in range(len(colours)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                screen.textinput(title="You've won!", prompt=f"The {winning_colour} turtle is the winner! Have fun?")
            else:
                screen.textinput(title="You've lost!", prompt=f"The {winning_colour} turtle is the winner! Have fun?")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
