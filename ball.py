from turtle import Turtle


class Ball():
    def __init__(self):
        self.color = 'lightsteelblue'
        self.ball = Turtle('circle')
        self.ball_building()
        self.x_move = 10
        self.y_move = 10

    def ball_building(self):
        self.ball.color(self.color)
        self.ball.pu()
        self.ball.shapesize(stretch_wid=0.75)
        self.ball.goto(0, -305)

    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce_off_brick(self):
        self.y_move *= -1

    def bounce(self):
        self.x_move *= -1

    def reset(self):
        self.ball.goto(0, -305)
        self.y_move = 10
        self.x_move = 10

