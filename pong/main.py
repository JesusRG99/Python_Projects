from turtle import Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

LEFT_RACKET_X_POS = -350
RIGHT_RACKET_X_POS = 350

# Creating Screen and set properties;
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Creates paddles and ball
l_paddle = Paddle((LEFT_RACKET_X_POS, 0))
r_paddle = Paddle((RIGHT_RACKET_X_POS, 0))
ball = Ball()
scoreboard = ScoreBoard()

# Key listeners to move paddles
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick() # Screen Exit on Click