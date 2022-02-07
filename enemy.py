from turtle import Turtle

DISTANCE_TO_MOVE_SIDEWAYS = 0.1
DISTANCE_TO_MOVE_DOWN = 0.1


class Enemy(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.setheading(180)
        self.is_alive = True

    def move_left(self):
        self.goto(self.xcor() - DISTANCE_TO_MOVE_SIDEWAYS, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + DISTANCE_TO_MOVE_SIDEWAYS, self.ycor())

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - DISTANCE_TO_MOVE_DOWN)

    def die(self):
        self.is_alive = False
        self.hideturtle()

