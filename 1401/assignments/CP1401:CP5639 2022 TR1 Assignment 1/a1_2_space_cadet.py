"""
CP1401 2022-2 Assignment 1
Program 2 - Space Cadet Results
Student Name: Mei Zhong
Date Started:

Pseudocode:
display "Welcome Trainee Space Cadet. How did you do?"
get practical_score, exam_score
total_score = practical_score + exam_score
display total score
if total_score <50
   display "You failed. Please try again next year."
else if plactical_score >= exam_score
    display "You will become a field agent."
else 
    display "You will become a desk officer."
if total_score >= 90
    display "You will become a field agent."
"""

print("Welcome Trainee Space Cadet. How did you do?")
practical_score = int(input("Practical score (0-50): "))
exam_score = int(input("     Exam score (0-50): "))
total_score = practical_score + exam_score
print(f"Your total score is {total_score} out of 100.")
if total_score < 50:
    print("You failed. Please try again next year.")
elif practical_score >= exam_score:
    print("You will become a field agent.")
else:
    print("You will become a desk officer.")

if total_score >= 90:
    print("Congratulations on making the honour roll!")