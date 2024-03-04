import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-230 - 10, y=y_positions[turtle_index])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You have guessed it right, {winning_color} has won")
            else:
                print(f"You have not guessed it right, {winning_color} has won")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
