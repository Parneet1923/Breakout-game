from turtle import Turtle


class Breaker():
    def __init__(self):
        self.color = 'deepskyblue'
        self.y = -320
        self.x = 0
        self.breaker = Turtle('square')
        self.breaker_building()

    def breaker_building(self):
        self.breaker.color(self.color)
        self.breaker.pu()
        self.breaker.goto(self.x, self.y)
        self.breaker.shapesize(stretch_len=6, stretch_wid=0.5)

    def move_forward(self):
        self.breaker.forward(20)

    def move_backward(self):
        self.breaker.back(20)

    def reset(self):
        self.breaker.goto(self.x, self.y)
