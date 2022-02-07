from turtle import Turtle

DISTANCE_TO_MOVE = 1


class Pellet(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.1, stretch_len=0.3)
        self.hideturtle()

    def move(self):
        while True:
            self.forward(DISTANCE_TO_MOVE)
