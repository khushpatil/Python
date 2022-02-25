from turtle import Screen
import turtle as t
from game_turtle import Game_Turtle
from scoreboard import Score
import pandas

screen = Screen()
screen.addshape("blank_states_image.gif")
t.shape("blank_states_image.gif")

tim = Game_Turtle()
tom = Score(-180,280)
terry = Score(-180,280)
theo = Score(-180,280)

states_data = pandas.read_csv("us_states.csv")
all_states = states_data['state'].to_list()
x_cor = states_data['x'].to_list()
y_cor = states_data['y'].to_list()

game_is_on = True
correct_ans = []
while game_is_on:
    ans = t.textinput("US States Game", "Guess the name of a state").capitalize()

    if ans in all_states:

        if ans not in correct_ans:
            print("You have guessed the correct answer!")
            correct_ans.append(ans)
            x_co = x_cor[all_states.index(ans)]
            y_co = y_cor[all_states.index(ans)]
            tim.correct_state(x_co,y_co,ans)
            terry.update_score(-50,280)

        else:
            print("You have already guessed that!")
            theo.update_lives()
    
    else:
        print("That is not a state!")
        theo.update_lives()
    
    if terry.rem_states == 0:
        print("Congrats, you have guessed all the states correctly!")
        game_is_on = False
    
    elif theo.lives == 0:
        print("Your lives are over, try again")
        game_is_on = False

    elif ans == "Exit":
        break