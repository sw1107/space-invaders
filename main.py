from functools import partial
from itertools import cycle
import random
from turtle import Screen
from player import Player
from enemy import Enemy
from scoreboard import Scoreboard
from player_pellet import PlayerPellet
from enemy_pellet import EnemyPellet


# TODO: build ability for player to die, change to new player
# TODO: build barriers
# TODO: make score change when player shoots enemy
# TODO: improve shooting to make it less jerky (try to build it into the class?)
# TODO: change player and enemy shapes to space invader shapes
# TODO: add sounds

ENEMY_MOVE_DISTANCE = 5
ENEMY_X_COORD_START = -170
ENEMY_Y_COORD_START = 200
ENEMY_X_COORD_CHANGE = 70
ENEMY_Y_COORD_CHANGE = 40

# ------------------- set up screen -------------------
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Space Invaders")

screen.tracer(0)

# ------------------- set up game board -------------------
player1 = Player()
player2 = Player()
player3 = Player()

player1.goto(x=0, y=-250)
player2.goto(x=-300, y=-350)
player3.goto(x=-350, y=-350)

player_pellets = []
enemy_pellets = []

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

scoreboard = Scoreboard()

screen.update()

# ------------------- create functionality -------------------


def create_player_pellet(player):
    new_pellet = PlayerPellet(player)
    player_pellets.append(new_pellet)


def create_enemy_pellet(enemy):
    new_pellet = EnemyPellet(enemy)
    enemy_pellets.append(new_pellet)


active_player = player1

screen.listen()
screen.onkey(active_player.move_left, "Left")
screen.onkey(active_player.move_right, "Right")
# screen.onkey(active_player.shoot, "space")
screen.onkey(partial(create_player_pellet, active_player), "space")

direction = cycle(["left", "right"])
current_direction = next(direction)

# ------------------- game play -------------------
while True:
    # move enemies
    if (current_direction == "left" and enemies[0].xcor() < -250) or \
            (current_direction == "right" and enemies[len(enemies) - 1].xcor() > 250):
        current_direction = next(direction)
        for enemy in enemies:
            enemy.move_down()
    elif current_direction == "left":
        for enemy in enemies:
            enemy.move_left()
    else:
        for enemy in enemies:
            enemy.move_right()

    # enemies shoot at random
    random_chance = random.randint(1, 500)
    if random_chance == 1:
        enemy_shooting = random.choice(enemies)
        create_enemy_pellet(enemy_shooting)

    # move pellets
    for pellet in player_pellets:
        if pellet.is_active:
            pellet.move()
            if pellet.ycor() > 400:
                pellet.hideturtle()
                pellet.is_active = False

    for pellet in enemy_pellets:
        if pellet.is_active:
            pellet.move()
            if pellet.ycor() < -250:
                pellet.hideturtle()
                pellet.is_active = False

    # detect player shooting enemy
    for enemy in enemies:
        for pellet in player_pellets:
            if pellet.is_active and enemy.is_alive:
                if pellet.distance(enemy) < 20:
                    pellet.is_active = False
                    pellet.hideturtle()
                    enemy.die()

    # detect enemy shooting player
    for pellet in enemy_pellets:
        if pellet.is_active:
            if pellet.distance(active_player) < 20:
                pellet.is_active = False
                active_player.hideturtle()
                print("player dead")

    screen.update()

# -------------------  -------------------
screen.exitonclick()
