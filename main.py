from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(width = 800, height=600)
screen.bgcolor("Black")
screen.title("Pong")

paddle = Paddle()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")

screen.exitonclick()