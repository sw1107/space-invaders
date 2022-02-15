from turtle import Turtle

PLAYER_DISTANCE_TO_MOVE = 10
PELLET_DISTANCE_TO_MOVE = 0.7
LIVES = 3
UPPER_BOUNDARY = 400


class PlayerController:

    def __init__(self):
        self.players = []
        self.player_pellets = []
        self.active_player = None

    def create_players(self):
        for _ in range(LIVES):
            new_player = Turtle()
            new_player.penup()
            new_player.color("#7CFC00")
            new_player.shape("square")
            new_player.shapesize(stretch_wid=1, stretch_len=1.5)
            new_player.setheading(180)
            self.players.append(new_player)
        self.players[0].goto(x=0, y=-250)
        self.players[1].goto(x=-350, y=-350)
        self.players[2].goto(x=-300, y=-350)
        self.active_player = self.players[0]

    def move_active_player_left(self):
        self.active_player.forward(PLAYER_DISTANCE_TO_MOVE)

    def move_active_player_right(self):
        self.active_player.backward(PLAYER_DISTANCE_TO_MOVE)

    def shoot(self):
        new_pellet = Turtle()
        new_pellet.hideturtle()
        new_pellet.penup()
        new_pellet.shape("square")
        new_pellet.shapesize(stretch_wid=0.1, stretch_len=0.3)
        new_pellet.setheading(90)
        new_pellet.goto(self.active_player.xcor(), self.active_player.ycor())
        new_pellet.color("#7CFC00")
        new_pellet.showturtle()
        self.player_pellets.append(new_pellet)

    def move_player_pellets(self):
        for pellet in self.player_pellets:
            if pellet.ycor() > UPPER_BOUNDARY:
                pellet.hideturtle()
                self.player_pellets.remove(pellet)
            else:
                pellet.forward(PELLET_DISTANCE_TO_MOVE)

    def remove_player(self):
        self.players[-1].hideturtle()
        self.players.remove(self.players[-1])

    def remove_player_pellet(self, pellet):
        pellet.hideturtle()
        self.player_pellets.remove(pellet)



