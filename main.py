import time
from turtle import Screen
from bricks import Brick
from breaker import Breaker
from ball import Ball
from scoreboard import Scoreboard, Lives


screen = Screen()
screen.setup(width=900, height=750)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

brick = Brick()
bricks_list = brick.bricks
breaker = Breaker()
ball = Ball()
scoreboard = Scoreboard()
lives = Lives()
game_on = True

screen.listen()
screen.onkey(breaker.move_forward, key="Right")
screen.onkey(breaker.move_backward, key="Left")

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    for item in bricks_list:
        if ball.ball.distance(item) < 40.75:
            if item.isvisible():
                ball.bounce_off_brick()
                item.hideturtle()
                scoreboard.increase_score()
    if ball.ball.xcor() > 420 or ball.ball.xcor() < -420:
        ball.bounce()
    if ball.ball.distance(breaker.breaker) < 26:
        ball.bounce_off_brick()
    if ball.ball.ycor() < -355:
        ball.reset()
        breaker.reset()
        lives.reduce()
    if ball.ball.ycor() > 355:
        ball.bounce_off_brick()
    if lives.lives == 0:
        ball.reset()
        breaker.reset()
        lives.reset_state()
        scoreboard.scoreboard_reset()
        for item in bricks_list:
            if not item.isvisible():
                item.showturtle()
        if scoreboard.score > scoreboard.high_score:
            scoreboard.high_score = scoreboard.score
            scoreboard.increase_high_score()

