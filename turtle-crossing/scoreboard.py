from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGMENT = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.goto(x=-280, y=250)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGMENT, font=FONT)
    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
