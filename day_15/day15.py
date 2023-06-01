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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.00


def printMenu():
    """Prints the list of drinks available and their price.

        Returns:
            None
    """
    for item in MENU:
        print(f"{item}, Cost: ${MENU[item]['cost']}.")


def printReport():
    for item in resources:
        print(f"{item}: {resources[item]} mL")
    print(f"${float('%.3g' % money)}")
    return


def checkResources(item):
    for i in MENU[item]["ingredients"]:
        if resources[i] - MENU[item]["ingredients"][i] <= 0:
            print(f"Insufficient {i}. ")
            return False
    return True


def getCoins(drink):
    print("Please Insert Coins.")
    coins = [int(input("How many quarters? ")) * 0.25, int(input("How many dimes? ")) * 0.1,
             int(input("How many nickels? ")) * 0.05, int(input("How many pennies? ")) * 0.01]

    total = float('%.2g' % sum(coins))

    if total > MENU[drink]["cost"]:
        print(f"Here is ${float('%.2g' % (total - MENU[drink]['cost']))} in change.")
        return True
    elif total == MENU[drink]["cost"]:
        return True
    else:
        print("Insufficient Funds. Returning coins.")
        return False


def run():
    global money

    while True:
        printMenu()

        choice = input("What would you like? ")

        if choice == "off":
            return
        elif choice == "print":
            printReport()
        elif choice in MENU.keys():
            if checkResources(choice):  # check resources
                if getCoins(choice):  # get money
                    for u, v in MENU[choice]["ingredients"].items():
                        resources[u] -= v
                    money += MENU[choice]["cost"]
                    print(f"Here is your {choice}. Enjoy!")
                else:
                    continue
            else:
                continue
        else:
            print("ERROR. Select again")

            printMenu()
