"""3. JCU Grades"""
import random

def main():
    score = float(input("Score: "))
    while score >= 0:
        grade = determine_grade(score)
        print(f"The grade of the score {score} is {grade}")
        score = float(input("Score: "))
    
    number_of_scores = int(input("How many random scores: "))
    for i in range(number_of_scores):
        random_score = random.randint(0, 100)
        grade = determine_grade(random_score)
        print(f"{random_score} = {grade}")


def determine_grade(score):
    if score < 50:
        grade = "F"
    elif score < 65:
        grade = "P"
    elif score < 75:
        grade = "C"
    elif score < 85:
        grade = "D"
    else:
        grade = "HD"

    return grade


def test_determine_grade():
    # boundary test
    score = 50
    grade = determine_grade(score)
    print(f"Score {score} should be P: {grade}")

    score = 65
    grade = determine_grade(score)
    print(f"Score {score} should be C: {grade}")

    score = 75
    grade = determine_grade(score)
    print(f"Score {score} should be D: {grade}")

    score = 85
    grade = determine_grade(score)
    print(f"Score {score} should be HD: {grade}")

    # Normal score test

    score = 40
    grade = determine_grade(score)
    print(f"Score {score} should be F: {grade}")

    score = 51
    grade = determine_grade(score)
    print(f"Score {score} should be P: {grade}")

    score = 70
    grade = determine_grade(score)
    print(f"Score {score} should be C: {grade}")

    score = 84
    grade = determine_grade(score)
    print(f"Score {score} should be D: {grade}")

    score = 90
    grade = determine_grade(score)
    print(f"Score {score} should be HD: {grade}")

    score = 100
    grade = determine_grade(score)
    print(f"Score {score} should be HD: {grade}")


# test_determine_grade()

main()


