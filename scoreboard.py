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
        self.goto(x=260, y=-360)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.level}    SCORE: {self.score}", align='center', font=FONT)

    def increase_score(self):
        self.score += SCORE_INCREASE
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()
