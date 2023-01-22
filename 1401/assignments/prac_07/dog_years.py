"""
Caculate dog years based on human years input

Pseudocode:
function main()
    get human_years
    while human_years >=0
        dog_years = calculate_dog_years(human_years)
        print dog_years
"""


def main():
    human_years = int(input("Age: "))
    while human_years >= 0:
        dog_years = calculate_dog_years(human_years)
        print(f"The dog years is {dog_years}")
        human_years = int(input("Age: "))


def calculate_dog_years(human_years):
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 21 + 4 * (human_years - 2)

    return dog_years


main()