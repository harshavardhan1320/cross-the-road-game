from turtle import Turtle

FONT = ("courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"level: {self.level} ", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over ", align="center", font=FONT)
