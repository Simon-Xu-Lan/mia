"""

Pseudocode:
get number of people
for loop of number of people
    get height
    get weight
    calculate BMI
    determin weight category
    open file bmis.txt for appending as out_file
    write BMI and category to out_file
    close out_file

open file bmis.txt for reading as in_file
for line in in_file
    print each line.
"""


def main():
    FILENAME = "bmis.txt"
    number_of_people = int(input("Number of people: "))
    for i in range(number_of_people):
        print(f"Person {i + 1}:")
        height = get_valid_number("Height (m): ", 0, 3)
        weight = get_valid_number("Weight (kg): ", 0, 300)
        bmi = calculate_bmi(height, weight)
        category = determine_weight_category(bmi)
        out_file = open(FILENAME, "a")
        out_file.write(f"BMI {bmi:.1f}, considered {category}\n")
        out_file.close()

    in_file = open(FILENAME, "r")
    for line in in_file:
        print(line.strip())
    in_file.close()


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


main()