from turtle import Turtle, colormode, Screen
import random

rainbow_colors = ["red", "green", "blue", "purple", "yellow", "orange"]
turtles = []
y_position = [-70, -40, -10, 20, 50, 80]
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

y_counter = -70
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(rainbow_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtles.append(new_turtle)
    y_counter +=30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost, The {winner} turtle won")
                
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()