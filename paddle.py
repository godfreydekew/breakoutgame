from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.left_pad_x = self.xcor() - 60
        self.right_pad_x = self.xcor() + 60
        self.penup()
        self.goto(position)

    def move_left(self):
        new_x = self.xcor() - 60
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 60
        self.goto(new_x, self.ycor())
