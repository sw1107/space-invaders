from turtle import Turtle

DISTANCE_TO_MOVE_SIDEWAYS = 0.1
DISTANCE_TO_MOVE_DOWN = 0.1
SPEED_INCREASE = 0.1


class Enemy(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.setheading(180)
        self.is_alive = True
        self.speed_sideways = DISTANCE_TO_MOVE_SIDEWAYS
        self.speed_downwards = DISTANCE_TO_MOVE_DOWN

    def move_left(self):
        self.goto(self.xcor() - self.speed_sideways, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.speed_sideways, self.ycor())

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.speed_downwards)

    def die(self):
        self.is_alive = False
        self.hideturtle()

    def speed_up(self):
        self.speed_sideways += SPEED_INCREASE
        self.speed_downwards += SPEED_INCREASE
