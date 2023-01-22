"""
Calculate a person's BMI and weight category

Pseudocode:
function main()
    height = 1.75
    for weight from 50 to 100 with step 2
        BMI = calculate_bmi(height, weight)
        weight_category = determine_weight_category(bmi)
        print BMI and weight_category
    for height 1.4m, 1.6m, 1.7m, 1.8m, 1.9m
        for weight 50, 60, 70, 80, 90, 100
            bmi = calculate_bmi(height, weight)
            weight_category = determine_weight_category(bmi)
            print BMI and weight_category

function calculate_bmi(height, weight)
    return weight / (height ** 2)

function determine_weight_category(bmi)
    if bmi < 18.5
        return underweight
    else if bmi < 25
        return normal
    else if bmi < 30
        return overweight
    else
        return obese
"""


def main():
    height = 1.75
    for weight in range(50, 101, 2):
        bmi = calculate_bmi(height, weight)
        weight_category = determine_weight_category(bmi)
        print(f"Height {height}m, Weight {weight}kg = BMI {bmi:.1f}, considered {weight_category}")
    print()
    for number in range(15, 20):
        height = number / 10
        for weight in range(50, 101, 10):
            bmi = calculate_bmi(height, weight)
            weight_category = determine_weight_category(bmi)
            print(f"Height {height}m, Weight {weight:3}kg = BMI {bmi:.1f}, considered {weight_category}")


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