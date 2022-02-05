#first exercise for day 3, conditional statements
#check whether a number is odd or even

# num = int(input("Enter your number: "))
# if num%2==0:
#     print("The number is an even number")
# else:
#     print("The number is an odd number")

#exercise 2: Improved BMI calculator with interpretation

# print("Welcome to the BMI calculator!")
# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kg: "))
# BMI = weight/(height**2)
# if(BMI<=18.5):
#     print("You are underweight")
# elif(BMI>18.5 and BMI <= 25):
#     print("You have a normal weight")
# elif(BMI>25 and BMI<=30):
#     print("You are overweight")
# elif(BMI>30 and BMI<=35):
#     print("You are obese")
# elif(BMI>35):
#     print("You are clinically obese")

#exercise 3 : Leap Year exercise
#Check whether a given year is leap year or not

# print("Welcome to the leap year checker!")
# year = int(input("Enter your year: "))
# if(year%4==0):
#     if(year%100==0):
#         if(year%400==0):
#             print(f"The year {year} is a leap year")
#         else:
#             print(f"The year {year} is not a leap year")
#     else:
#         print(f"The year {year} is a leap year")
# else:
#     print(f"The year {year} is not a leap year")

#exercise 4 : pizza order program

# print("Welcome to python Pizza!")
# sp = 15
# mp = 20 
# lp = 25
# spep = 5
# lpep = 10
# ch = 1
# pepp = input("Small Price = $5\n""Medium and Large price = $10\n""Do you want extra pepperoni?(y/n): ")
# cheese = input("Extra cheese price = $1\n""Do you want extra cheese?(y/n): ")
# size = input("Small Price = $15\n""Medium Price = $20\n""Large Price = $25\n""Enter the size of pizza you want: ")
# if(size == "small"):
#     bill = sp
#     if(pepp == "y"):
#         bill += spep
#     if(cheese == "y"):
#         bill += ch
# elif(size == "medium"):
#     bill =mp
#     if(pepp == "y"):
#         bill += lpep
#     if(cheese == "y"):
#         bill += ch
# elif(size == "large"):
#     bill =lp
#     if(pepp == "y"):
#         bill += lpep
#     if(cheese == "y"):
#         bill += ch
# print(f"Your bill is ${bill}")

#exercise 5 : love calculator

# print("This is the love calculator")
# name1 = input("What is your name?: ")
# name2  = input("What is their name?: ")
# tnum = name1.count("t") + name2.count("t")
# rnum = name1.count("r") + name2.count("r")
# unum = name1.count("u") + name2.count("u")
# enum = name1.count("e") + name2.count("e")
# lnum = name1.count("l") + name2.count("l")
# onum = name1.count("o") + name2.count("o")
# vnum = name1.count("v") + name2.count("v")
# true = tnum+rnum+unum+enum
# love = lnum+onum+vnum+enum
# per = str(true) + str(love)
# if(int(per) < 10 and int(per) > 90):
#     print(f"Your score is {per}, you go together like coke and mentos")
# elif(int(per) >= 40 and int(per) <= 50):
#     print(f"Your score is {per}, you are alright together")
# else:
#     print(f"Your score is {per}")

#Final project for day 3
# print("Welcome to treasure island, your mission is to find the treasure")
# dir = input("Where do you want to go, left or right?(l/r):  ")
# if(dir == "l"):
#     act = input("Would you like to swim or wait?(s/w): ")
#     if(act == "w"):
#         door = input("Which door would you like to open?(r,b or y): ")
#         if(door == "y"):
#             print("congrats you found the treasure!")
#         else:
#             print("game over")
#     else:
#         print("game over")
# else:
#     print("game over")