from turtle import Turtle
from random import choice


class Brick():
    def __init__(self):
        self.shape = 'square'
        self.colors = ['firebrick', 'gold', 'darkorange', 'green']
        self.bricks = []
        self.x = -400
        self.y = 270
        self.color_code = -1
        self.bricks_building()

    def brick_building(self, x, y, color):
        new_segment = Turtle(shape=self.shape)
        new_segment.color(color)
        new_segment.shapesize(stretch_len=3)
        new_segment.pu()
        new_segment.goto(x, y)
        self.bricks.append(new_segment)

    def bricks_building(self):
        for i in range(8):
            self.x = -402
            if i % 2 == 0:
                self.color_code += 1
            for i in range(11):
                self.brick_building(self.x, self.y, self.colors[self.color_code])
                self.x += 80
            self.y -= 30

    def delete_brick(self, index):
        self.bricks.pop(index)





