from turtle import Turtle
FONT = ("Arial", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.score = 0
        self.color('white')
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.goto(0, 300)
        self.write(f"Score: {self.score} High score: {self.high_score}", align='center', font=FONT)

    def increase_score(self):
        self.score += 10
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align='center', font=FONT)

    def increase_high_score(self):
        with open('data.txt', mode='w') as data:
            data.write(str(self.high_score))

    def scoreboard_reset(self):
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align='center', font=FONT)

class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.lives = 3
        self.color('White')
        self.goto(380, 305)
        self.write(f'Lives: {self.lives}', align='center', font=('Arial', 20, 'normal'))

    def reduce(self):
        self.lives -= 1
        self.clear()
        self.write(f'Lives: {self.lives}', align='center', font=('Arial', 20, 'normal'))

    def reset_state(self):
        self.lives = 3
        self.clear()
        self.write(f'Lives: {self.lives}', align='center', font=('Arial', 20, 'normal'))


