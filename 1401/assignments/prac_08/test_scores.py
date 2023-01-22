"""
a program that asks the user to enter 4 test scores between 0 and 100,
then displays a JCU grade for each score and also the average test score.

Pseudocode:
scores = empty list
for i in range(4)
    get score
    add the score to scores
    determine grade
    display score and grade
calculate average score
display average score
"""


# Code
def main():
    NUMBER_OF_SCORE = 4
    scores = []
    for i in range(NUMBER_OF_SCORE):
        score = get_valid_number(f"Score {i + 1}: ", 0, 100)
        scores.append(score)

    for score in scores:
        grade = determine_grade(score)
        print(f"Score {score}, which is {grade}")
    average_score = sum(scores) / len(scores)
    print(f"The average score was {average_score:.3f}")
    if scores[-1] > average_score:
        print("The trend is positive")
    else:
        print("The trend is not positive")


def determine_grade(score):
    if score < 50:
        grade = "N"
    elif score < 65:
        grade = "P"
    elif score < 75:
        grade = "C"
    elif score < 85:
        grade = "D"
    else:
        grade = "HD"

    return grade


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number

main()
