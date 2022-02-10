#Grading program using dictionaries
# student_scores = {
#     "Harry":81,
#     "Ron":78,
#     "Hermione":99,
#     "Draco":74,
#     "Neville":62,
# }
# student_grades = {}
# def grade_assign(dc):
#     grade = ""
#     for key in dc:
#         score = dc[key]
#         if(score<70):
#             grade = "Fail"
#         elif(score>=70 and score<80):
#             grade = "Acceptable"
#         elif(score>=80 and score<90):
#             grade = "Exceeds Expectations"
#         else:
#             grade = "Outstanding"
#         student_grades[key] = grade
# grade_assign(student_scores)
# print(student_grades)

#another exercise on nesting of dictionaries and lists
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# def add_new_country(country, visit_num, cities):    
#     new_dic["country"] = country
#     new_dic["visits"] = visit_num
#     new_dic["cities"] = cities
#     travel_log.append(new_dic)
# ans = "y"
# while ans == "y":
#     num_visits = 0
#     new_dic = {}
#     cities = []
#     country = input("Enter the name of the country you visited: ")
#     visit_num = int(input("Enter the number of times you have visited that country: "))
#     num_visits = int(input("How many cities have you visited: "))
#     print("Now enter the names of the cities visited\n")
#     for i in range(num_visits):
#         cities.append(input(""))
#     add_new_country(country, visit_num, cities)
#     ans = input("Do you want to add another country?(y/n): ")
# print(travel_log)

#The blind bidding program
import os
import art
def add_bidder(name,bid):
    new_bid = {}
    new_bid["Name"] = name
    new_bid["Bid"] = bid
    bid_list.append(new_bid)
def compare_bid(bid_list):
    greatest_bid = {"Name": " ", "Bid": 0}
    for bidder in bid_list:
        if(bidder["Bid"]>greatest_bid["Bid"]):
            greatest_bid = bidder.copy()
    return greatest_bid

print(art.logo)
winner = {}
print("Welcome to the silent bid")
bid_list = []
ans = "y"
while ans == "y":
    name = input("Please enter your name: ")
    bid = int(input("Enter your bid: "))
    add_bidder(name,bid)
    ans = input("Is there any other bidder?(y/n): ")
    os.system("cls") 
else:
    winner = compare_bid(bid_list)
    print(winner["Name"] + " is the winner, with a bid of",winner["Bid"] )
