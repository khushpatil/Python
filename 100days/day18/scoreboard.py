from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0
        self.pencolor("white")
        self.up()

    def draw_line(self):
        self.setpos(-400,0)
        self.pensize(width=5)
        for _ in range(40):
            self.down()
            self.fd(10)
            self.up()
            self.fd(10)

    def update_score(self,position):
        self.setpos(position)
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align = "center", font = ("Arial",24,"normal"))