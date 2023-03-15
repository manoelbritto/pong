from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(width = 800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle('game1')
paddle2 = Paddle('game2')

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()