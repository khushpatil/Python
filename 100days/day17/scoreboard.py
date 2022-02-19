from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.score_num = 0
        self.setpos(int(-30),260)
        self.pencolor("white")
        self.write("Score: ",self.score_num,align="center",font = ("Arial",24,"normal"))
        self.up()
        self.setpos(50,260)
        self.down()

    def update_score(self):
        self.clear()
        self.score_num += 1
        self.write(self.score_num,align="right",font = ("Arial",24,"normal"))