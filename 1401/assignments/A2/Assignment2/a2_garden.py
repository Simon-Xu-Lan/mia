"""
CP1401 2022-1 Assignment 2
Market Garden Simulator
Student Name: Mei Zhong
Date started: Jan 25 2023


Pseudocode:
Display welcome message, instructions, and initial plants
display menu
get valid menu choice
while choice != Q
    if choice == "W"
        simulates a day
        get random rainfall
        determine a random plant die if not enough rain
        each plan generates an amount of food
    if choice == "D"
        display plants in my garden.
    if choice == "A"
        add new plant
    get valid menu choice
show final details, plants, number of days, number of plants, the amount of food
be prompted to save the plants, one per line, to a file
"""


import random

LOW_RAINFALL = 0
HIGH_RAINFALL = 128
RAINFALL_THRESHOLD = 32


def main():
    """
    Display welcome message, instuctions, initial plants, and menus.
    """

    day_count = 0
    total_food_amount = 0
    plants = []
    print("Welcome to my garden.")
    print("Plants cost and generate food according to their name length (e.g., Sage plants cost 4).")
    print("You can buy new plants with the food your garden generates.")
    print(f"You get up to {HIGH_RAINFALL} mm of rain per day. Not all plants can survive with less than {RAINFALL_THRESHOLD}.")
    print("Enjoy :)")
    get_initial_plants(plants)
    display_status(plants, day_count, total_food_amount)
    choice = choose_menu()
    while choice != "Q":
        if choice == "W":
            rainfall = create_rain(LOW_RAINFALL, HIGH_RAINFALL)
            total_food_amount += simulate_plant(plants, rainfall, RAINFALL_THRESHOLD, HIGH_RAINFALL)
            day_count += 1
        elif choice == "A":
            total_food_amount -= add_new_plant(plants, total_food_amount)
        elif choice == "D":
            display_plants(plants)
            print()
        display_status(plants, day_count, total_food_amount)
        choice = choose_menu()
    wrap_up(plants, day_count, total_food_amount)





def get_initial_plants(plants):
    """
    Add plants list with a list of plants from plants.txt if user choose load, otherwise create a list of plants
    :return: the list of plants
    """
    is_load_plants = input("Would you like to load your plants from plants.txt (Y/n)? ").upper()
    if is_load_plants == "N":
        some_plants = ["Parsley", "Sage", "Rosemary", "Thyme",]
        print("You start with these plants:")
        plants.extend(some_plants)
        display_plants(plants)
        # Move cursor to new line
        print()
    else:
        print("Loaded")
        file = open("plants.txt", "r")
        for line in file:
            line = line.strip("\n")
            if line != "":
                plants.append(line)
        file.close()
        display_plants(plants)
        print("Now I Have Lots")
    # print empty line
    print()


def display_status(plants, days, amount):
    """Display current status of days, plants, and food amount"""
    print(f"After {days} days, you have {len(plants)} plants and your total food is {amount}")

def display_plants(plants):
    """
    plants: a list of plants
    is_loaded: True means load plants from file plants.txt
    print the list of plants.
    """
    for plant in plants:
        print(plant, end=", ")


def choose_menu():
    """
    Display menu, Get valid user choice from menu.
    """
    menus = ["(W)ait", "(D)isplay plants", "(A)dd new plant", "(Q)uit"]
    for menu in menus:
        print(menu)
    user_choice = input("Choose: ").upper()
    while user_choice not in "WDAQ":
        print("Invalid choice")
        user_choice = input("Choose: ").upper()
    return user_choice


def create_rain(low, high):
    """Generate random rainfall betwwen low and high"""
    random_rainfall = random.randint(low, high)
    print(f"Rainfall: {random_rainfall}")
    return random_rainfall


def choose_died_plant(plants):
    """
    Randomly choose a plant from plants to die.
    return the died plant plant
    """
    number = random.randint(0, len(plants) - 1)
    died_plant = plants[number]
    print(f"Sadly, your {died_plant} plant has died")
    return died_plant


def simulate_plant(plants, rainfall, threshold, high_rain):
    """
    remove a plant from the list of plants if rainfall is less than threshold
    Each plant generates an amount of food according to a formula
    return the total of food produced.
    return 0 is plants is empty
    """
    total_food_produced = 0
    if len(plants) > 0:
        if rainfall < threshold:
            died_plant = choose_died_plant(plants)
            plants.remove(died_plant)
        # calculate percent according to a formula provided
        percent = random.randint(int(rainfall / 3), rainfall) / high_rain
        for plant in plants:
            food_produced = int(len(plant) * percent)
            print(f"{plant} produced {food_produced}", end=", ")
            total_food_produced += food_produced
        # move cursor to next line
        print()
    return total_food_produced


def test_simulate_plant():
    """Test funciton simulate_plant"""
    my_plants = ["Parsley", "Sage", "Rosemary", "Thyme"]
    rainfalls = [30, 32, 98, 128]
    print(my_plants)
    for rainfall in rainfalls:
        print(f"Rainfall: {rainfall}")
        amount = simulate_plant(my_plants, rainfall, 32, 128)
        print(f"Food amount: {amount}")
        print(my_plants)


def get_valid_plant():
    """
    Get valid plant name. New plant names cannot be blank
    return valid plant name.
    """
    plant = input("Enter plant name: ").title()
    while plant == "":
        print("Invalid plant name")
        plant = input("Enter plant name: ").title()
    return plant


def add_new_plant(plants, total_amount):
    """
    Add valid plant name to the list of plants.
    If plant name is already in plants list, ask user to input another plant name.
    return cost reduction.
    """
    new_plant = get_valid_plant()
    cost = len(new_plant)
    while new_plant in plants:
        print(f"You already have a {new_plant} plant.")
        new_plant = get_valid_plant()
    if cost > total_amount:
        print(f"Ok would cost {cost} food. With only {total_amount}, you can't afford it.")
        reduction = 0
    else:
        plants.append(new_plant)
        reduction = cost
    return reduction


def save_plants(plants, file):
    """save the plants, one per line, to a file call plants.txt"""
    f = open(file, 'w')
    for plant in plants:
        f.write(plant + "\n")
    f.close()


def wrap_up(plants, days, amount):
    """
    show the final details including the plants, the number of days simulated, the number of plants and the amount of food.
    then be prompted to save the plants to a file.
    """
    if len(plants) == 0:
        print("You finished with no plants")
    else:
        print("You finished with these plants:")
        display_plants(plants)
        print()
    display_status(plants, days, amount)
    is_save_plants = input("Would you like to save your plants to plants.txt (Y/n)? ").upper()
    if is_save_plants != "N":
        save_plants(plants, "plants.txt")
        print("saved")
    print("Thank you for simulating. Now enjoy some real plants.")


main()

# test_simulate_plant()