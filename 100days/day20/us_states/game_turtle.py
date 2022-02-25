from turtle import Turtle

class Game_Turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        
    def correct_state(self,x,y,ans):
        self.up()
        self.setpos(x,y)
        self.down()
        self.write(ans,align = "center",font = ("Arial", 7, "normal"))
        self.up()

