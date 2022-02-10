from functools import partial
from itertools import cycle
import random
from turtle import Screen
from player import Player
from enemy import Enemy
from scoreboard import Scoreboard
from player_pellet import PlayerPellet
from enemy_pellet import EnemyPellet

# add game reset, increase level, and increase speed with level
# TODO: build barriers
# TODO: change player and enemy shapes to space invader shapes
# TODO: add sounds
# TODO: can the create pellet functions be a part of a class?

ENEMY_MOVE_DISTANCE = 5
ENEMY_X_COORD_START = -170
ENEMY_Y_COORD_START = 200
ENEMY_X_COORD_CHANGE = 70
ENEMY_Y_COORD_CHANGE = 40
KILL_DISTANCE = 18
LIVES = 3

global players
global player_pellets
global enemy_pellets
global enemies
global active_player

# ------------------- set up screen -------------------
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Space Invaders")

screen.tracer(0)

screen.listen()

scoreboard = Scoreboard()
# ------------------- create functionality -------------------


def create_player_pellet(player):
    new_pellet = PlayerPellet(player)
    player_pellets.append(new_pellet)


def create_enemy_pellet(enemy):
    new_pellet = EnemyPellet(enemy)
    enemy_pellets.append(new_pellet)


direction = cycle(["left", "right"])
current_direction = next(direction)

# ------------------- set up game board -------------------


def reset_game():
    global players
    global player_pellets
    global enemy_pellets
    global enemies
    global active_player

    try:
        for pellet in player_pellets:
            pellet.remove_from_screen()
    except NameError:
        pass

    try:
        for pellet in enemy_pellets:
            pellet.remove_from_screen()
    except NameError:
        pass

    try:
        for player in players:
            player.hideturtle()
        players.clear()
    except NameError:
        pass

    players = [Player() for _ in range(LIVES)]

    players[0].goto(x=0, y=-250)
    players[1].goto(x=-350, y=-350)
    players[2].goto(x=-300, y=-350)

    player_pellets = []
    enemy_pellets = []

    enemies = []
    x_coord = ENEMY_X_COORD_START
    y_coord = ENEMY_Y_COORD_START
    for i in range(3):
        for j in range(6):
            new_enemy = Enemy(scoreboard.level)
            new_enemy.goto(x=x_coord, y=y_coord)
            enemies.append(new_enemy)
            x_coord += ENEMY_X_COORD_CHANGE
        x_coord = ENEMY_X_COORD_START
        y_coord -= ENEMY_Y_COORD_CHANGE

    active_player = players[0]

    screen.onkey(active_player.move_left, "Left")
    screen.onkey(active_player.move_right, "Right")
    screen.onkey(partial(create_player_pellet, active_player), "space")

    screen.update()


# ------------------- game play -------------------

reset_game()
is_game_on = True
while is_game_on:
    # move enemies
    if (current_direction == "left" and enemies[0].xcor() < -250) or \
            (current_direction == "right" and enemies[len(enemies) - 1].xcor() > 250):
        for enemy in enemies:
            enemy.move_down()
            print(enemies[0].xcor())
        current_direction = next(direction)
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
                pellet.remove_from_screen()

    # detect player shooting enemy
    for enemy in enemies:
        for pellet in player_pellets:
            if pellet.is_active and enemy.is_alive and pellet.distance(enemy) < KILL_DISTANCE:
                pellet.remove_from_screen()
                enemy.die()
                enemies.remove(enemy)
                scoreboard.increase_score()
                if len(enemies) == 0:
                    scoreboard.level_up()
                    reset_game()

    # detect enemy shooting player
    for pellet in enemy_pellets:
        if pellet.is_active and pellet.distance(active_player) < KILL_DISTANCE:
            pellet.remove_from_screen()
            players[-1].hideturtle()
            players.remove(players[-1])
            if len(players) == 0:
                is_game_on = False
                scoreboard.game_over()

    screen.update()

# -------------------  -------------------
screen.exitonclick()
