from turtle import Turtle

class Blocks(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1.6, stretch_len=6.38)
        self.penup()
        self.goto(position)
        # Defining borders of the brick
        self.left_wall = self.xcor() - 16
        self.right_wall = self.xcor() + 16
        self.upper_wall = self.ycor() + 65
        self.bottom_wall = self.ycor() - 65


