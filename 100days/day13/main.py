# from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("DarkSlateBlue")
# print(my_screen.canvheight)
# timmy.forward(100)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon",["Pikachu", "Raichu", "Squirtle"])
# table.add_column("Type", ["ELectric", "Electric", "Water"])
# table.align = "r"
# print(table)

#Coffee Machine using objects and classes
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine 
import os
def main():
    mobj = Menu()
    cmobj = CoffeeMaker()
    mmobj = MoneyMachine()
    print("Welcome to the coffee shop!")
    is_on = True
    while is_on:
        action = input("Type y to order a coffee or report to get the reports or n to exit: ")
        if action == "y":
            print(mobj.get_items())
            order = mobj.find_drink(input("Which drink would you like to order: "))
            if order != None:
                if cmobj.is_resource_sufficient(order):
                    if mmobj.make_payment(order.cost):
                        cmobj.make_coffee(order)
                    else:print("The money is refunded because it is insufficient")
                else:print(f"We don't have enough resources for {order.name}!")
            else:print(f"This {order.name} does not exist")

        elif action == "report":
            which_report = input("Type r to get the resources report or m to get the profit report: ")
            if which_report == "r":
                cmobj.report()
            elif which_report == "m":
                mmobj.report()
            else: return "Invalid Operation"

        else:
            is_on = False
            os.system("cls")
            if input("Type y to go back to the starting question or n to exit: ") == "y":
                main()
main()


