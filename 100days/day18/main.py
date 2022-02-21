from turtle import Screen
from board import Board
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")

board1 = Board()
board2 = Board()

score = Score()
score_up = Score()
score_down = Score()

ball = Ball()
ball.speed(0)

board1.setpos(0,290)
board2.setpos(0,int(-280))

score.draw_line()

screen.listen()

screen.onkey(fun = board1.move_right, key = "Right")
screen.onkey(fun = board1.move_left, key = "Left")

screen.onkey(fun = board2.move_right, key = "d")
screen.onkey(fun = board2.move_left, key = "a")

def initialize():
    time.sleep(2)
    board1.setpos(0,290)
    board2.setpos(0,int(-280))
    ball.setpos(0,0)

game_is_on =True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    if ball.distance(board1) < 50 and ball.ycor() >= 280:
        ball.bounce()
    if ball.distance(board2) < 50 and ball.ycor() <= -260:
        ball.bounce()
    if ball.xcor() >= 380 or ball.xcor() <= -380:
        ball.bounce2() 
    if ball.ycor() >= 300:
        score_down.update_score((-380,-60))
        initialize()
    if ball.ycor() <= -290:
        score_up.update_score((-380,20))
        initialize()
        












screen.exitonclick()