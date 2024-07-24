MENU = {
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}

def check_resources(recipie):
    for resource in MENU[recipie]["ingredients"]:
        if resources[resource] < MENU[recipie]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}")
            return False
    return True

def make_coffee(recipie):
    for resource in MENU[recipie]["ingredients"]:
        resources[resource] -= MENU[recipie]["ingredients"][resource]
    print(f"Here is your {recipie} ☕. Enjoy!")      

def coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

machine_on = True

while machine_on:
    print(f"Coffee Machine Report: ")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
    drink = input(("What would you like? (espresso/latte/cappuccino): ")).lower()
    if check_resources(drink)==True:
        sum = coins() 
        pay = round(sum - MENU[drink]["cost"])
        profit += MENU[drink]["cost"]
        print(f"Here is ${pay} in change.")
        make_coffee(drink)
    else:
        machine_on = False           
