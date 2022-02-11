import os
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

cash = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25,
}

def print_report(resources):
    print(f'Water = {resources["water"]}ml\nMilk = {resources["milk"]}ml\nCoffee = {resources["coffee"]}g\nMoney = {resources["money"]}')

def make_coffee(coffee_type, resources):
    if coffee_type == "espresso":
        resources["water"] -= menu["espresso"]["ingredients"]["water"]
        resources["coffee"] -= menu["espresso"]["ingredients"]["coffee"]
        resources["money"] += menu["espresso"]["cost"]
    elif coffee_type == "latte":
        resources["water"] -= menu["latte"]["ingredients"]["water"]
        resources["milk"] -= menu["latte"]["ingredients"]["milk"]
        resources["coffee"] -= menu["latte"]["ingredients"]["coffee"]
        resources["money"] += menu["latte"]["cost"]
    elif coffee_type == "cappuccino":
        resources["water"] -= menu["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= menu["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= menu["cappuccino"]["ingredients"]["coffee"]
        resources["money"] += menu["cappuccino"]["cost"]
    else:print("Sorry, we don't make that coffee in here")

def check_resources(coffee_type, resources):
    if coffee_type == "espresso":
        if(resources["water"]>=menu["espresso"]["ingredients"]["water"]
            and resources["coffee"]>=menu["espresso"]["ingredients"]["coffee"]):
            return True
    elif coffee_type == "latte":
        if(resources["water"]>=menu["latte"]["ingredients"]["water"]
            and resources["coffee"]>=menu["latte"]["ingredients"]["coffee"]
            and resources["milk"]>=menu["latte"]["ingredients"]["milk"]):
            return True
    elif coffee_type == "cappuccino":
        if(resources["water"]>=menu["cappuccino"]["ingredients"]["water"]
            and resources["coffee"]>=menu["cappuccino"]["ingredients"]["coffee"]
            and resources["milk"]>=menu["cappuccino"]["ingredients"]["milk"]):
            return True
    else:print("We don't serve that coffee in here")

def process_payment(cash, coffee_type,resources):
    payment = {}
    tot_given = 0
    print("Please make the payment in coins\nHow many of each will you be giving?")
    for i in cash:
        payment[i] = float(input(f"How many {i} will you be giving?: "))
    for i in payment:
        if(i == "penny"):
            tot_given += cash[i] * payment[i]
        if(i == "nickel"):
            tot_given += cash[i] * payment[i]
        if(i == "dime"):
            tot_given += cash[i] * payment[i]
        if(i == "quarter"):
            tot_given += cash[i] * payment[i]
    if(coffee_type == "espresso"):
        bill = menu["espresso"]["cost"]
    elif coffee_type == "latte":
        bill = menu["latte"]["cost"]
    elif coffee_type == "cappuccino":
        bill = menu["cappuccino"]["cost"]
    if(tot_given < bill):
        print("You have paid less than the cost so we are refunding you")
        payment.clear()
    else:
        resources["money"] += menu[coffee_type]["cost"]
        print(f"The bill is {bill} and you have paid {round(tot_given,2)}, so the change amount is {round(tot_given-bill,2)}, here you go!\nEnjoy your {coffee_type}!")
        payment.clear()
    
def main():
    print("Welcome to the coffee shop!")
    action = input("Type y to order a coffee or report to check resources or n to quit: ")
    if action == "y":
        for i in menu:
            print(i)
        coffee_type = input("Which coffee would you like to have: ").lower()
        if check_resources(coffee_type,resources):
            make_coffee(coffee_type,resources)
            process_payment(cash,coffee_type,resources)
        else:
            print("We don't have enough resources for that coffee!")
    elif action == "report":
        print_report(resources)
    else:
        os.system("cls")
    f_action = input("Type y to go back to the starting question or n to quit: ")
    if f_action == "y":
        main()

main()