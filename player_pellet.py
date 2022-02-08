from turtle import Turtle

DISTANCE_TO_MOVE = 0.7


class PlayerPellet(Turtle):

    def __init__(self, player):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.1, stretch_len=0.3)
        self.setheading(90)
        self.goto(player.xcor(), player.ycor())
        self.color("#7CFC00")
        self.showturtle()
        self.is_active = True

    def move(self):
        self.forward(DISTANCE_TO_MOVE)

    def remove_from_screen(self):
        self.is_active = False
        self.hideturtle()