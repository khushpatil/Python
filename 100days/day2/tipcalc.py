print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: \n"))
people = float(input("How many people are splitting the bill?: \n"))
per = float(input("What percentage of bill would you like to tip?: \n"))
tip = (bill*per)/100
tot = tip+bill
pp =tot/people
print("The bill per person will be ",pp)