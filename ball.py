from turtle import Turtle

class Ball (Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(1.5,1.5)
        self.goto(position)
        self.penup()

        # self.move()

    def move(self):
        new_x = self.xcor()+10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)