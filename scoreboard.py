from turtle import Turtle

FONT = ("Helvetica", 20, "bold")
SCORE_INCREASE = 10


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=260, y=-360)
        self.clear()
        self.write(f"LEVEL: {self.level}  SCORE: {self.score}", align='center', font=FONT)
        self.display_high_score()

    def increase_score(self):
        self.score += SCORE_INCREASE
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)
        if self.score > self.high_score:
            with open("high_score.txt", "w") as file:
                file.write(str(self.score))
            self.goto(0, -30)
            self.write(f"NEW HIGH SCORE: {self.score}", align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def display_high_score(self):
        self.goto(x=-280, y=340)
        self.write(f"HIGH SCORE: {self.high_score}", align='center', font=FONT)

