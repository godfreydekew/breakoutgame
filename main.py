from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from blocks import Blocks
from borders import Borders

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.title("My BreakOut Game")
screen.tracer(0)
my_blocks = []

# Create borders
lower_border = Borders((0, -300), 0.1, 40)
upper_border = Borders((0, 300), 0.1, 40)
left_border = Borders((-400, 0), 30, 0.1)
right_border = Borders((400, 0), 30, 0.1)

# Create the ball, paddle, and scoreboard
ball = Ball()
my_paddle = Paddle((0, -270))
scoreboard = Scoreboard()

# Set up keyboard controls for the paddle
screen.listen()
screen.onkey(my_paddle.move_left, "Left")
screen.onkey(my_paddle.move_right, "Right")

# Create a list of colored blocks
total_width = 800
gap = 5  # 5-pixel gap between blocks
num_blocks = 6
block_width = (total_width - (gap * (num_blocks - 1))) / num_blocks

# Create and position the blocks
x_position = -total_width / 2 + block_width / 2

for i in range(6):
    block1 = Blocks((x_position, 20), "red")
    block2 = Blocks((x_position, 60), "blue")
    block3 = Blocks((x_position, 100), "yellow")
    block4 = Blocks((x_position, 140), "green")
    block5 = Blocks((x_position, 180), "purple")
    my_blocks.append(block1)
    my_blocks.append(block2)
    my_blocks.append(block3)
    my_blocks.append(block4)
    my_blocks.append(block5)
    x_position += block_width + gap

game_is_on = True
while game_is_on:
    screen.update()

    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with the top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with the left and right walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect when the ball goes below the paddle
    if ball.ycor() < -300:
        scoreboard.update_life()
        ball.reset_position()

    # Detect collision with the paddle
    if ball.distance(my_paddle) < 70:
        if ball.ycor() < -240:
            ball.bounce_y()

    # Detect collision with the blocks
    for block in my_blocks:
        if ball.distance(block) < 66:
            if ball.xcor() < block.left_wall:
                block.goto(3000, 3000)  # Move block out of sight
                ball.bounce_x()

            if ball.xcor() < block.right_wall:
                block.goto(3000, 3000)
                ball.bounce_x()

            if ball.ycor() > block.bottom_wall:
                block.goto(3000, 3000)
                ball.bounce_y()
            scoreboard.update_score()
            ball.speed_update()

    # Check for game over condition (no lives left)
    if scoreboard.life == 0:
        game_is_on = False
        scoreboard.game_over()

# Close the game when clicking on the screen
screen.exitonclick()
