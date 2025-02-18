from turtle import Turtle, Screen, colormode
import random
rgb_colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), 
              (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), 
              (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), 
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), 
              (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), 
              (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), 
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]
colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.goto(-125,0)

def painting(size):
    for column in range(size):
        last_position = [tim.position()[0], tim.position()[1]]
        for row in range(size):
            tim.dot(20, random.choice(rgb_colors))
            tim.forward(50)
        tim.teleport(-125,last_position[1]+50)

painting(10)   
screen = Screen()
screen.exitonclick()