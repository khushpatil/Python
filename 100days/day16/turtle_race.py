#Etch a Sketch Program
from turtle import Turtle, Screen
import turtle
import random
# tim = Turtle()
# screen = Screen()
# screen.listen()
# def move_fd():
#     tim.fd(10)
# def move_bk():
#     tim.bk(10)
# def turn_cw():
#     head = tim.heading()
#     tim.seth(head+10)
# def turn_anticw():
#     head = tim.heading()
#     tim.seth(head-10)
# def clear():
#     tim.setpos(0,0)
#     tim.seth(0)
#     tim.clear()
# screen.onkey(key = "w", fun = move_fd)
# screen.onkey(key = "s", fun = move_bk)
# screen.onkey(key = "d", fun = turn_cw)
# screen.onkey(key = "a", fun = turn_anticw)
# screen.onkey(key = "c", fun = clear)
# screen.exitonclick()

#Turtle Race Game

colors = ["red", "blue", "green", "orange", "yellow"]

screen = Screen()
screen.listen()
num_turtles = int(input("How many turtles do you want?: "))
print(f"Creating {num_turtles} turtles with random colors...")
turtles = []
def t_create(num_turtles,turtles):
    for _ in range(num_turtles):
        new_turt = Turtle()
        new_turt.color(colors[_])
        new_turt.shape("turtle")
        turtles.append(new_turt)

def start_position():
    x_co = -(screen.window_width()/2)
    y_co = -200
    for turtle in turtles:
        turtle.up()
        turtle.setpos(int(x_co+50),int(y_co))
        y_co += 50

def race(user_bet):
    is_on = True
    while is_on:
        for turtle in turtles:
            if turtle.xcor() > 310:
                is_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print("Congrats your turtle has won!")
                else: print(f"Your turtle has lost, the winning turtle is {winning_color} turtle")
            step = random.randint(1,15)
            turtle.fd(step)

def main():
    t_create(num_turtles, turtles)
    start_position()
    user_bet = screen.textinput(title = "Make your bet", prompt = "Which color turtle will win?: ")
    race(user_bet)

main()

screen.exitonclick()

