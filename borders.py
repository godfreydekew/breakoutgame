from turtle import Turtle



class Borders(Turtle):
    def __init__(self, position, y, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=y, stretch_len=x)
        self.left_pad_x = self.xcor() - 60
        self.right_pad_x = self.xcor() + 60
        self.penup()
        self.goto(position)