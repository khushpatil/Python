from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.score_num = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.setpos(int(-30),260)
        self.pencolor("white")
        self.write(f"Score:   High Score: ",align="center",font = ("Arial",24,"normal"))
        self.up()
        self.setpos(50,260)
        self.down()

    def update_score(self):
        self.clear()
        self.up()
        self.setpos(-60,260)
        self.down()
        self.write(self.score_num,align="right",font = ("Arial",24,"normal"))
        self.up()
        self.setpos(150,260)
        self.down()
        self.write(self.high_score,align="right",font = ("Arial",24,"normal"))

    def reset(self):
        if self.score_num > self.high_score:
            self.high_score = self.score_num
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score_num = 0
        self.update_score()