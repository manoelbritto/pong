from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle(Turtle):
    def __init__(self, start):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        if start == 'game1':
            self.goto(350, 0)
        else:
            self.goto(-350, 0)


    def up(self):
        newy = self.ycor()+20
        self.goto(self.xcor(), newy)

    def down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)