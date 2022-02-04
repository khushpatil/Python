#The final project for day 2

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill?: \n"))
# people = float(input("How many people are splitting the bill?: \n"))
# per = float(input("What percentage of bill would you like to tip?: \n"))
# tip = (bill*per)/100
# tot = tip+bill
# pp =tot/people
# print("The bill per person will be ",pp)

#Below is just a small exercise to add the digits in a number entered by the user
#Also the first exercise for day 2

# num = input("Enter your number: ")
# res = 0
# for i in range(len(num)):
#     res = res + int(num[i])
# print("The result is: ",res)

#Below is a BMI calculator, also the second exercise for day 2
# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kg: "))
# BMI = int(weight/(height**2))
# print("Your BMI is ",BMI)

#Here is a sadistic exercise to tell you how much time you have left to live
#if you luckily turn out to live for 90 years

# age = float(input("What is your current age?: "))
# years = 90 - age
# months = years * 12
# weeks = years * 52
# days = years * 365
# print(f"You have {years} years, {months} months, {weeks} weeks and {days} days left to live.")