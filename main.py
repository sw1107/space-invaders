from turtle import Screen
from scoreboard import Scoreboard
from enemy_controller import EnemyController
from player_controller import PlayerController

# TODO: change player and enemy shapes to space invader shapes
# TODO: add sounds
# TODO: build barriers

KILL_DISTANCE = 18

# ------------------- set up screen -------------------
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Space Invaders")

screen.tracer(0)

screen.listen()

scoreboard = Scoreboard()

# ------------------- create controllers -------------------
enemy_controller = EnemyController()
player_controller = PlayerController()

# ------------------- create players and add functionality -------------------
player_controller.create_players()
screen.onkey(player_controller.move_active_player_left, "Left")
screen.onkey(player_controller.move_active_player_right, "Right")
screen.onkey(player_controller.shoot, "space")


# ------------------- set up game board -------------------


def reset_game():
    for pellet in player_controller.player_pellets:
        player_controller.remove_player_pellet(pellet)

    for pellet in enemy_controller.enemy_pellets:
        enemy_controller.remove_enemy_pellet(pellet)

    enemy_controller.create_enemies(scoreboard.level)

    screen.update()


# ------------------- game play -------------------

reset_game()
is_game_on = True
while is_game_on:

    enemy_controller.move_enemies()

    enemy_controller.shoot_at_random()

    enemy_controller.move_enemy_pellets()

    player_controller.move_player_pellets()

    # detect player shooting enemy
    for enemy in enemy_controller.enemies:
        for pellet in player_controller.player_pellets:
            if pellet.distance(enemy) < KILL_DISTANCE:
                player_controller.remove_player_pellet(pellet)
                enemy_controller.remove_enemy(enemy)
                scoreboard.increase_score()
                if len(enemy_controller.enemies) == 0:
                    scoreboard.level_up()
                    reset_game()

    # detect enemy shooting player
    for pellet in enemy_controller.enemy_pellets:
        if pellet.distance(player_controller.active_player) < KILL_DISTANCE:
            enemy_controller.remove_enemy_pellet(pellet)
            player_controller.remove_player()
            if len(player_controller.players) == 0:
                is_game_on = False
                scoreboard.game_over()

    screen.update()

# -------------------  -------------------
screen.exitonclick()
