from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-200, 320)
        self.score = 0
        self.life = 10
        self.write(f"Score:{self.score}      Life:{self.life}", font=("Courier", 20, "normal"))

    def update_life(self):
        self.clear()
        self.life -= 1
        self.write(f"Score:{self.score}      Life:{self.life}", font=("Courier", 20, "normal"))
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score}      Life:{self.life}", font=("Courier", 20, "normal"))
    def game_over(self):
        self.goto(-100, -100)
        self.write(f"GAME OVER!!\nScore:{self.score} ", font=("Courier", 30, "bold"), align="center", move=False)
        self.color("red")
