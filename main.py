from functools import partial
from turtle import Screen
from player import Player
from enemy import Enemy
from scoreboard import Scoreboard
from pellet import Pellet
from enemy_controller import EnemyController

ENEMY_MOVE_DISTANCE = 5
ENEMY_X_COORD_START = -170
ENEMY_Y_COORD_START = 200
ENEMY_X_COORD_CHANGE = 70
ENEMY_Y_COORD_CHANGE = 40


# TODO: build ability for player to shoot <-----
# TODO: build ability for enemies to shoot
# TODO: build ability for enemy to die
# TODO: build ability for player to die, change to new player
# TODO: make score change when player shoots enemy
# TODO: change player and enemy shapes to space invader shapes

# ------------------- set up screen -------------------
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Space Invaders")

screen.tracer(0)

# ------------------- set up game -------------------
player1 = Player()
player2 = Player()
player3 = Player()

player1.goto(x=0, y=-250)
player2.goto(x=-300, y=-350)
player3.goto(x=-350, y=-350)

player_pellets = []

enemies = []
x_coord = ENEMY_X_COORD_START
y_coord = ENEMY_Y_COORD_START
for i in range(3):
    for j in range(6):
        enemy = Enemy()
        enemy.goto(x=x_coord, y=y_coord)
        enemies.append(enemy)
        x_coord += ENEMY_X_COORD_CHANGE
    x_coord = ENEMY_X_COORD_START
    y_coord -= ENEMY_Y_COORD_CHANGE

# enemy_controller = EnemyController()
# enemy_controller.create_enemies()

scoreboard = Scoreboard()

screen.tracer(1)

# ------------------- create functionality -------------------
active_player = player1

screen.listen()
screen.onkey(active_player.move_left, "Left")
screen.onkey(active_player.move_right, "Right")
screen.onkey(active_player.shoot, "space")
# screen.onkey(partial(), "space")

# ------------------- make enemies move -------------------
while True:
    has_reached_left_wall = False
    while not has_reached_left_wall:
        for enemy in enemies:
            enemy.move_left()
            if enemy.xcor() < -250:
                has_reached_left_wall = True
    for enemy in enemies:
        enemy.move_down()
    has_reached_right_wall = False
    while not has_reached_right_wall:
        for enemy in enemies:
            enemy.move_right()
            if enemy.xcor() > 250:
                has_reached_right_wall = True
    for enemy in enemies:
        enemy.move_down()

    # if ... move enemies

    # if pellet in player_pellets, move it up
# -------------------  -------------------


# -------------------  -------------------
screen.exitonclick()
