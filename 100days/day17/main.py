from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score
import sys

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)
tim = Snake()
tim.create_snake()
food = Food()
score = Score()
up_score = Score()
screen.update()

screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.left, "Left")
screen.onkey(tim.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    tim.move()
    if tim.head.distance(food) < 15 :
        food.refresh()
        tim.grow()
        up_score.score_num += 1
        up_score.update_score()
    
    if tim.head.xcor() == 300 or tim.head.xcor() == -300 or tim.head.ycor() == 300 or tim.head.ycor() == -300:
        time.sleep(2)
        tim.reset_snake()
        up_score.reset()          

    for snake in tim.len_snake:
        if snake == tim.head:
            pass
        elif tim.head.distance(snake) < 10:
            time.sleep(2)
            tim.reset_snake()
            up_score.reset()










screen.exitonclick()