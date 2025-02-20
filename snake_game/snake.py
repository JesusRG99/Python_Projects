from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_HEADING = 90
DOWN_HEADING = 270
LEFT_HEADING = 180
RIGHT_HEADING = 0

class Snake():
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.xpos = self.head.xcor()
        self.ypos = self.head.ycor()
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
            self.segment = Turtle("square")
            self.segment.color("white")
            self.segment.penup()
            self.segment.goto(position)
            self.snake_segments.append(self.segment)
    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
    def reset(self):
        for segment in self.snake_segments:
            segment.goto(1000,1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
    def move(self):
        for seg_number in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_number -1].xcor()
            new_y = self.snake_segments[seg_number -1].ycor()
            self.snake_segments[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN_HEADING:
            self.head.setheading(UP_HEADING)
    def down(self):
        if self.head.heading() != UP_HEADING:
            self.head.setheading(DOWN_HEADING)
    def left(self):
        if self.head.heading() != RIGHT_HEADING:
            self.head.setheading(LEFT_HEADING)
    def right(self):
        if self.head.heading() != LEFT_HEADING:
            self.head.setheading(RIGHT_HEADING)
        