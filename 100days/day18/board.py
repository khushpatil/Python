from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.color("white")
        self.up()

    def move_right(self):
        if self.xcor() < 300 or self.xcor() > -300:
            self.fd(20)

    def move_left(self):
        self.bk(20)

     