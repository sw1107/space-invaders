from functools import partial
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from player_pellet import PlayerPellet
from enemy_controller import EnemyController


# add README
# refactor code to use enemy_controller object
# TODO: refactor code to use player_controller object
# TODO: update README

# TODO: change player and enemy shapes to space invader shapes
# TODO: add sounds
# TODO: build barriers

KILL_DISTANCE = 18
LIVES = 3

global players
global player_pellets
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

enemy_controller = EnemyController(scoreboard.level)


def create_player_pellet(player):
    new_pellet = PlayerPellet(player)
    player_pellets.append(new_pellet)

# ------------------- set up game board -------------------


def reset_game():
    global players
    global player_pellets
    global active_player

    try:
        for pellet in player_pellets:
            pellet.remove_from_screen()
    except NameError:
        pass

    try:
        for pellet in enemy_controller.enemy_pellets:
            pellet.hideturtle()
            enemy_controller.enemy_pellets.remove(pellet)
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

    enemy_controller.create_enemies()

    active_player = players[0]

    screen.onkey(active_player.move_left, "Left")
    screen.onkey(active_player.move_right, "Right")
    screen.onkey(partial(create_player_pellet, active_player), "space")

    screen.update()


# ------------------- game play -------------------

reset_game()
is_game_on = True
while is_game_on:

    enemy_controller.move_enemies()

    enemy_controller.shoot_at_random()

    # move pellets
    for pellet in player_pellets:
        if pellet.is_active:
            pellet.move()
            if pellet.ycor() > 400:
                pellet.hideturtle()
                pellet.is_active = False

    enemy_controller.move_enemy_pellets()

    # detect player shooting enemy
    for enemy in enemy_controller.enemies:
        for pellet in player_pellets:
            if pellet.is_active and pellet.distance(enemy) < KILL_DISTANCE:
                pellet.remove_from_screen()
                enemy.hideturtle()
                enemy_controller.enemies.remove(enemy)
                print(len(enemy_controller.enemies))
                scoreboard.increase_score()
                if len(enemy_controller.enemies) == 0:
                    scoreboard.level_up()
                    reset_game()

    # detect enemy shooting player
    for pellet in enemy_controller.enemy_pellets:
        if pellet.distance(active_player) < KILL_DISTANCE:
            pellet.hideturtle()
            enemy_controller.enemy_pellets.remove(pellet)
            players[-1].hideturtle()
            players.remove(players[-1])
            if len(players) == 0:
                is_game_on = False
                scoreboard.game_over()

    screen.update()

# -------------------  -------------------
screen.exitonclick()
