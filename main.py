MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

machine = True


def report():
    return f"Water: {resources.get('water')} \nMilk: {resources.get('milk')} \nCoffee: {resources.get('coffee')} \nMoney: {resources.get('money')} "


def coins():
    number_of_quarters = float(input("Number of quarters? "))
    number_of_dimes = float(input("Number of dimes? "))
    number_of_nickles = float(input("Number of nickles? "))
    number_of_pennies = float(input("Number of pennies? "))
    added_money = (number_of_pennies * PENNY) + (number_of_nickles * NICKLE) + (number_of_dimes * DIME) + (number_of_quarters * QUARTER)
    return added_money


def check_resources(coffee):
    global machine
    if MENU.get(coffee).get("ingredients").get("water") < resources.get("water"):
        if MENU.get(coffee).get("ingredients").get("milk") < resources.get("milk"):
            if MENU.get(coffee).get("ingredients").get("coffee") < resources.get("coffee"):
                return True
            else:
                print("Don't have enough coffee. Money refunded. ")
                machine = False
        else:
            print("Don't have enough milk. Money refunded. ")
            machine = False
    else:
        print("Don't have enough water. Money refunded. ")
        machine = False


def check_money(coffee, money):
    price_of_coffee = MENU.get(coffee).get("cost")

    if money > price_of_coffee:
        change = round(money - price_of_coffee,2)
        print(f"Here is ${change} in change.")
        print(f"Enjoy your {coffee}!")
    elif money == price_of_coffee:
        print(f"Here is your {coffee}. Enjoy!")
    elif money < price_of_coffee:
        print(f"Sorry that's not enough money. Money refunded. ")


while machine:
    option = input("What would you like? espresso/latte/cappuccino: ").lower()

    if option == "report":
        print(report())
    elif option == "off":
        print("Turning off! Bye!")
        machine = False
    else:
        money = coins()
        if check_resources(option):
            check_money(option, money)
            karel = resources["money"] + MENU.get(option).get("cost")
            resources["money"] = karel
            water_difference = resources["water"] - MENU.get(option).get("ingredients").get("water")
            resources["water"] = water_difference
            milk_difference = resources["milk"] - MENU.get(option).get("ingredients").get("milk")
            resources["milk"] = milk_difference
            coffee_difference = resources["coffee"] - MENU.get(option).get("ingredients").get("coffee")



