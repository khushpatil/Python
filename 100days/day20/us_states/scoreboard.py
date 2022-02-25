from turtle import Turtle

class Score(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.ht()
        self.up()
        self.pensize(width=3)
        self.setpos(x,y)
        self.down()
        self.rem_states = 50
        self.write(f"Remaining States: ",align = "center", font = ("Arial", 20,"normal"))
        self.lives = 5

    def update_score(self,x,y):
        self.rem_states -= 1
        self.clear()
        self.up()
        self.setpos(x,y)
        self.down()
        self.write(self.rem_states,align = "center", font=("Arial",20, "normal"))

    def update_lives(self):
        self.lives -= 1
        self.clear()
        self.up()
        self.setpos(80,280)
        self.down()
        self.write(f"Lives remaining: {self.lives}",align= "center", font=("Arial",20,"normal"))