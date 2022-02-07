from turtle import Turtle

DISTANCE_TO_MOVE = 0.7


class EnemyPellet(Turtle):

    def __init__(self, enemy):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.1, stretch_len=0.3)
        self.setheading(270)
        self.goto(enemy.xcor(), enemy.ycor())
        self.color("white")
        self.showturtle()
        self.is_active = True

    def move(self):
        self.forward(DISTANCE_TO_MOVE)
