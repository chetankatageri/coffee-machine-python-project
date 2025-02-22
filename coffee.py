from random import choice

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(resources, ingridientss):
    for items in ingridientss:
        if ingridientss[items] <= resources[items]:
            return True
        else:
            print('insufficient resources')


def process_coins():
    total = 0
    total += int(input("enter no of quaters")) * 0.25
    total += int(input("enter no of dimes")) * 0.10
    total += int(input("enter no of nickes")) * 0.05
    total += int(input("enter no of pemies")) * 0.01
    return total


def transactions_successful(totall, price):
    if totall < price:
        print("insufficient funds")
        return False
    else:
        chance = totall - price
        print(f"here is your change {chance}")
        print(f"here is your coffee")
        return True


def coffee_machine():
    ON = True
    while ON:

        choice = input('what would you like?(espresso/latte/cappaccino)')

        if choice == 'OFF':
            ON = False
        elif choice == 'report':
            for resource in resources:
                print(resource + ':' + resources[resource])
        elif choice in MENU:
            ingridientss = MENU[choice]["ingredients"]
            price = MENU[choice]["cost"]

            check_r = check_resources(resources, ingridientss)
            totall = process_coins()
            t_s = transactions_successful(totall, price)
            return coffee_machine()


coffee_machine()









