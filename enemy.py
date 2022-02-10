from turtle import Turtle

DISTANCE_TO_MOVE_SIDEWAYS = 0.2
DISTANCE_TO_MOVE_DOWN = 0.5


class Enemy(Turtle):

    def __init__(self, level):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.setheading(180)
        self.is_alive = True
        self.speed_sideways = DISTANCE_TO_MOVE_SIDEWAYS * level
        self.speed_downwards = DISTANCE_TO_MOVE_DOWN * level

    def move_left(self):
        self.goto(self.xcor() - self.speed_sideways, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.speed_sideways, self.ycor())

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.speed_downwards)

    def die(self):
        self.is_alive = False
        self.hideturtle()

