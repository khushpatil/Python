#Exercise 1 to format names
# def format_name(f_name,l_name):
#     new_fname = f_name.title()
#     new_lname = l_name.title()
#     new_full_name = new_fname + " " + new_lname
#     return new_full_name
# f_name = input("Please enter your first name: ")
# l_name = input("Please enter your last name: ")
# print(f"Your full name is {format_name(f_name,l_name)}")

#Exercise 2 : Leap Year days and months
# def check_leap(year):
#     if(year%4==0):
#         if(year%100==0):
#             if(year%400==0):
#                 return True
#             else:return False
#         else:return True
#     else:return False
# def days_in_month(year,month):
#     if month > 12 or month < 1:
#         return "Invalid Input"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     leap = check_leap(year)
#     if leap:
#         month_days[1] = 29
#     return month_days[month - 1]


# num_days = days_in_month(int(input("Which year are you in?: ")), int(input("Which month do you want to know?: ")))
# print(f"There are {num_days} days in your selected month for that year")  

#Main Project: Calculator
import os
def calculator(n1,op,n2):
    if(op == "+"):
        return n1+n2
    elif(op == "-"):
        return n1-n2
    elif(op == "*"):
        return n1*n2
    elif(op == "/"):
        return n1/n2
    else:return "Not a valid operation"

def main():
    num1 = int(input("Enter the first number: "))
    keep_going = True
    while keep_going:
        opr = input("Which operation do you want to perform(+, -, *, /): ")
        num2 = int(input("Enter the second number: "))
        result = calculator(num1, opr, num2)
        print(f"{num1} {opr} {num2} = {result}")
        if(input("Type y to keep going or n to start a new calculation: ")) == "y":
            num1 = result
        else:
            keep_going = False
            os.system("cls")
            main()

main()
