"""
All Together now
This is a coffee ordering program with a menu, a fixed list of valid coffees to
check orders agains, and instructions for making the selected coffee.
The program is able to drink coffee virtually, and because some people can't decide,
it is able to choose randomly from the menu.

Algorithm
display welcome message
display menu
get valid choice
while choice != "Q"
    if choice == "D"
        drink coffee
        if customer didn't order coffee
            display "Oh... where's my coffee?"
        else
            drink coffee virtually
    else if choise == "O"
        display coffee options
        get vaild coffee choice
        make coffee
    else if choice == "R"
        get random coffee choice
        make coffee
    else
        get valid choice
display "Thanks for drinking coffee"

funciton drink coffee
    if customer didn't order coffee
            return "Oh... where's my coffee?"
        else
            return "Mmmm, nice {coffee choice}"

function make coffee
    display steps according to choice
"""

import random


def main():
    coffee_choice = ""
    print("Welcome to the IT@JCU Coffee Shop")
    choice = choose_menu()
    while choice != "Q":
        if choice == "D":
            drink_coffee(coffee_choice)
        elif choice == "O":
            coffee_choice = choose_coffee()
            make_coffee(coffee_choice)
        elif choice == "R":
            coffee_choice = choose_coffee_randomly()
            make_coffee(coffee_choice)
        choice = choose_menu()
    print("Thanks for drinking coffee")


def choose_menu():
    choice = input("(O)rder - (D)rink - (R)andom choice - (Q)uit\n>>> ").upper()
    while choice not in "ODRQ":
        print("Invalid option")
        choice = input("(O)rder - (D)rink - (R)andom choice - (Q)uit\n>>> ").upper()
    return choice


def drink_coffee(choice):
    if choice != "":
        print(f"Mmmm, nice {choice.title()}")
    else:
        print("Oh... where's my coffee?")


def choose_coffee():
    coffee_options = ['FLAT WHITE', 'ESPRESSO', 'LONG BLACK', 'BABYCCINO']
    print("Please choose from:")
    my_coffee = input("Flat White - Espresso - Long Black - Babyccino - ? ").upper()
    while my_coffee not in coffee_options:
        print("Invalid order")
        my_coffee = input("? ").upper()
    return my_coffee


def make_coffee(choice):
    """Print making coffee steps according to coffee choice"""
    print(f"Here's how to make a/n {choice.title()}:")
    if choice == "Flat White".upper():
        grind_coffee_beans()
        add_espresso()
        steam_milk()
        add_milk()
    elif choice == "Espresso".upper():
        grind_coffee_beans()
        add_espresso()
    elif choice == "Long Black".upper():
        grind_coffee_beans()
        add_espresso()
        print("- Add hot water to cup")
    elif choice == "Babyccino".upper():
        steam_milk()
        add_milk()
    else:  # Unexpected case
        print("Something went wrong! Unknown coffee.")


def grind_coffee_beans():
    """Print steps for grinding the coffee beans."""
    print("- Insert portafilter into grinder")
    print("- Press grind button to grind beans into portafilter")


def add_espresso():
    """Display steps for making espresso"""
    print("- Distribute grounds")
    print("- Tamp grounds")
    print("- Insert full portafilter into group head")
    print("- Press shot button to pour espresso into cup")


def steam_milk():
    """Print instructions for steaming milk."""
    print("- Fill jug with milk")
    print("- Steam milk until nice microfoam formed and milk up to temperature")


def add_milk():
    """Print instructions for adding milk."""
    print("- Swirl milk gently in jug")
    print("- Pour milk into cup... carefully, artistically :)")


def choose_coffee_randomly():
    coffee_options = ['FLAT WHITE', 'ESPRESSO', 'LONG BLACK', 'BABYCCINO']
    i = random.randint(0, len(coffee_options))
    return coffee_options[i]

main()