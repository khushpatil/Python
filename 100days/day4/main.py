#Exercise 1 : Head or tails
# import random
# randomint = random.randint(0,1)
# if(randomint == 0):
#     print("This is a tails")
# else:
#     print("This is a heads")

#exercise 2 : who is going to buy the meal
# import random
# names =[]
# num_people = int(input("How many people are attending the dinner?: "))
# for i in range(num_people):
#     names.append(input("Who all are sitting at the table?: "))
# randnum = random.randint(0,num_people-1)
# print(f"The one to pay the bill will be {names[randnum]}!")

#exercise 3 : treasure marking system

# row1 = [" "," "," "]
# row2 = [" "," "," "]
# row3 = [" "," "," "]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# h = int(input("Enter the horizontal column number: "))
# v = int(input("Enter the vertical column number: "))
# map[h-1][v-1] = "x"
# print(f"{row1}\n{row2}\n{row3}") 

#final project of day 4 : a rock, paper, scissors game with the computer
# import random
# print("This is the rock, paper, scissors game!")
# print("0 will be rock, 1 will be paper and 2 will be scissors!\nMake your choice!")
# choices = ["rock", "paper", "scissors"]
# choice = int(input("Enter your choice: "))
# cpu_choice = random.randint(0,2)
# while choice == 0:
#     if(cpu_choice == 0):
#         print(f"Your choice is {choices[choice]} and the cpu choice is {choices[cpu_choice]}\nThis is a draw!")
#     elif(cpu_choice == 1):
#         print(f"Your choice is {choices[choice]} and the cpu choice is {choices[cpu_choice]}\nThe cpu wins!")
#     else:
#         print(f"Your choice is {choices[choice]} and the cpu choice is {choices[cpu_choice]}\nCongrats, you win!") 
#     break
# while choice == 1:
#     if(cpu_choice == 0):
#         print(f"Your choice is {choices[choice]} and the cpu choice is {choices[cpu_choice]}\nCongrats, you win!")
#     elif(cpu_choice == 1):
#         print(f"Your choice is {choices[choice]} and the cpu choice is {choices[cpu_choice]}\nThis is a draw!")
#     else:
#         print(f"Your choice is {choices[choice]} and the cpu choice is {choices[cpu_choice]}\nThe cpu wins!")
#     break
# while choice == 2:
#     if(cpu_choice == 0):
#         print(f"Your choice is {choices[choice]} and the cpu choice is {choices[cpu_choice]}\nThe cpu wins!")
#     elif(cpu_choice == 1):
#         print(f"Your choice is {choices[choice]} and the cpu choice is {choices[cpu_choice]}\nCongrats, you win!")
#     else:
#         print(f"Your choice is {choices[choice]} and the cpu choice is {choices[cpu_choice]}\nThis is a draw!")
#     break
# else:
#     print("Nigga please type any number between 0,1 and 2 and nothing else please")
