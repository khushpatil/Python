#Creating a blackjack game with the computer
import random
import os
def draw(hand,cards):
    hand.append(random.choice(cards))
    print(f"The hand is: {hand}")
def det_winner(psum,csum):
    if(psum == 21 and csum == 21):
        print("This is a tie!")
    elif(psum == 21):
        print("The player has won the game!")
    elif(csum == 21):
        print("The computer has won the game!")
    elif(psum > 21 and csum < 21):
        print("The computer has won the game!")
    elif(psum < 21 and csum > 21):
        print("The player has won the game!")
    elif(psum < 21 and csum < 21):
        if(psum > csum):
            print("The player has won the game!")
        elif(psum == csum):
            print("This is a tie!")
        else:print("The computer has won the game!")
def main():
    while input("To play a blackjack game press y or n to quit: ") == "y":
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        player_hand = []
        player_sum = 0
        comp_hand = []
        comp_sum = 0
        for i in range(2):
            player_hand.append(random.choice(cards))
        comp_hand.append(random.choice(cards))
        print(f"Your hand is: {player_hand}\nThe computer's hand is: {comp_hand}")
        player_sum = sum(player_hand)
        play = True
        while player_sum < 21 and play:
            action = input("Type hit to get another card or pass to pass to computer: ")
            if action == "hit":
                draw(player_hand,cards)
                player_sum = sum(player_hand)
            elif action == "pass":
                draw(comp_hand,cards)
                comp_sum = sum(comp_hand)
                if comp_sum < 17:
                    draw(comp_hand,cards)
                comp_sum = sum(comp_hand)
                play = False
            else:
                print("You can only hit or pass and nothing else")
        det_winner(player_sum, comp_sum)
        if(input("To play once again press y or n to quit: ") == "y"):
            os.system("cls")
            main()
        else:
            os.system("cls")

main()