from turtle import Turtle

FONT = ("Helvetica", 20, "bold")
SCORE_INCREASE = 10

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=290, y=-360)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}", align='center', font=FONT)

    def increase_score(self):
        self.score += SCORE_INCREASE
        self.update_scoreboard()
