# Day 16: Object Oriented Programming
# Building the Coffee Machine in OOP

from day_16.menu import Menu, MenuItem
from day_16.coffee_maker import CoffeeMaker
from day_16.money_machine import MoneyMachine


def run():
    # Create objects
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    # Start the coffee machine
    is_on = True

    while is_on:
        # Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        choice = input(f"What would you like? ({menu.get_items()}): ")

        # Turn off the Coffee Machine by entering “off” to the prompt.
        if choice == "off":
            is_on = False

        # Print report
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()

        # Check resources sufficient?
        else:
            drink = menu.find_drink(choice)
            if drink is not None and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
                    drink.cost):
                coffee_maker.make_coffee(drink)
