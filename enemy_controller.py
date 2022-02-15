from turtle import Turtle
from itertools import cycle
import random

ENEMY_X_COORD_START = -170
ENEMY_Y_COORD_START = 200
ENEMY_X_COORD_CHANGE = 70
ENEMY_Y_COORD_CHANGE = 40

ENEMY_DISTANCE_TO_MOVE_SIDEWAYS = 0.2
ENEMY_DISTANCE_TO_MOVE_DOWN = 1

PELLET_DISTANCE_TO_MOVE = 0.7
LOWER_BOUNDARY = -250

direction = cycle(["left", "right"])


class EnemyController:

    def __init__(self):
        self.enemies = []
        self.speed_sideways = 0
        self.speed_downwards = 0
        self.current_direction = next(direction)
        self.enemy_pellets = []

    def create_enemies(self, level):
        x_coord = ENEMY_X_COORD_START
        y_coord = ENEMY_Y_COORD_START
        for i in range(3):
            for j in range(6):
                new_enemy = Turtle()
                new_enemy.penup()
                new_enemy.color("white")
                new_enemy.shape("square")
                new_enemy.shapesize(stretch_wid=1, stretch_len=1.5)
                new_enemy.setheading(180)
                new_enemy.goto(x=x_coord, y=y_coord)
                self.enemies.append(new_enemy)
                x_coord += ENEMY_X_COORD_CHANGE
            x_coord = ENEMY_X_COORD_START
            y_coord -= ENEMY_Y_COORD_CHANGE
        self.speed_downwards = ENEMY_DISTANCE_TO_MOVE_DOWN * level
        self.speed_sideways = ENEMY_DISTANCE_TO_MOVE_SIDEWAYS * level

    def move_enemies(self):
        if (self.current_direction == "left" and self.enemies[0].xcor() < -300) or \
                (self.current_direction == "right" and self.enemies[len(self.enemies) - 1].xcor() > 300):
            for enemy in self.enemies:
                # move down
                enemy.goto(enemy.xcor(), enemy.ycor() - self.speed_downwards)
            self.current_direction = next(direction)
        elif self.current_direction == "left":
            for enemy in self.enemies:
                # move left
                enemy.goto(enemy.xcor() - self.speed_sideways, enemy.ycor())
        else:
            for enemy in self.enemies:
                # move right
                enemy.goto(enemy.xcor() + self.speed_sideways, enemy.ycor())

    def shoot_at_random(self):
        random_chance = random.randint(1, round(500/self.speed_downwards))
        if random_chance == 1:
            random_enemy = random.choice(self.enemies)
            self.create_enemy_pellet(random_enemy)

    def create_enemy_pellet(self, enemy):
        new_pellet = Turtle()
        new_pellet.hideturtle()
        new_pellet.penup()
        new_pellet.shape("square")
        new_pellet.shapesize(stretch_wid=0.1, stretch_len=0.3)
        new_pellet.setheading(270)
        new_pellet.goto(enemy.xcor(), enemy.ycor())
        new_pellet.color("white")
        self.enemy_pellets.append(new_pellet)
        new_pellet.showturtle()

    def move_enemy_pellets(self):
        for pellet in self.enemy_pellets:
            if pellet.ycor() < LOWER_BOUNDARY:
                pellet.hideturtle()
                self.enemy_pellets.remove(pellet)
            else:
                pellet.forward(PELLET_DISTANCE_TO_MOVE)

    def remove_enemy(self, enemy):
        enemy.hideturtle()
        self.enemies.remove(enemy)

    def remove_enemy_pellet(self, pellet):
        pellet.hideturtle()
        self.enemy_pellets.remove(pellet)