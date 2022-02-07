from turtle import Turtle

DISTANCE_TO_MOVE = 10
X_COORD_START = -170
Y_COORD_START = 150
X_COORD_CHANGE = 70
Y_COORD_CHANGE = 40

class EnemyController:

    def __init__(self):
        self.enemies = []

    def create_enemies(self):
        x_coord = X_COORD_START
        y_coord = Y_COORD_START
        for i in range(3):
            for j in range(6):
                enemy = Turtle("square")
                enemy.penup()
                enemy.color("white")
                enemy.shapesize(stretch_wid=1, stretch_len=1.5)
                enemy.setheading(180)
                enemy.goto(x=x_coord, y=y_coord)
                self.enemies.append(enemy)
                x_coord += X_COORD_CHANGE
            x_coord = X_COORD_START
            y_coord -= Y_COORD_CHANGE




