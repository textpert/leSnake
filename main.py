from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")

snake = Snake()
screen.tracer(0)
screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.left,key="a")
screen.onkey(fun=snake.down,key="s")
screen.onkey(fun=snake.right,key="d")

# # TODO move the segments in forward direction
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    game_on = snake.move_snake()
#
#
#
# # TODO add controls for snake
#
# screen.onkey(fun=move_up, key="w")
# screen.onkey(fun=move_left, key="d")
# screen.onkey(fun=move_right, key="a")



screen.exitonclick()
