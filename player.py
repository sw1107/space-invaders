from turtle import Turtle

DISTANCE_TO_MOVE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("#7CFC00")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.setheading(180)

    def move_left(self):
        self.forward(DISTANCE_TO_MOVE)

    def move_right(self):
        self.backward(DISTANCE_TO_MOVE)

