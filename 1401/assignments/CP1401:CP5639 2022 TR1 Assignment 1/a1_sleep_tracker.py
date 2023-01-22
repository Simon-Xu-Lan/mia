"""
CP1401 2022-2 Assignment 1
Program 3 - Sleep Tracker
Student Name: Mei Zhong
Date Started:

Pseudocode:
PERIOD_OF_DAYS = 5
DESIRABLE_HOURS_OF_SLEEP_PER_DAY = 8
recommended_total_sleep_hours = DESIRABLE_HOURS_OF_SLEEP_PER_DAY * PERIOD_OF_DAYS
total_hours_of_sleep = 0
display "Sleep Tracker"
for day from 1 to PERIOD_OF_DAYS
    get hours_of_sleep
    while hours_of_sleep < 0 or hours_of_sleep > 24
        display invalid number of hours
        get hours_of_sleep
    total_hours_of_sleep = total_hours_of_sleep + hours_of_sleep 
sleep_debt = recommended_total_sleep_hours - total_hours_of_sleep
display empty line
display recommended_total_sleep_hours
display total_hours_of_sleep
display sleep debt
"""

PERIOD_OF_DAYS = 5
DESIRABLE_HOURS_OF_SLEEP_PER_DAY = 8
recommended_total_sleep_hours = DESIRABLE_HOURS_OF_SLEEP_PER_DAY * PERIOD_OF_DAYS
total_hours_of_sleep = 0
print("Sleep Tracker")
for day in range(1, PERIOD_OF_DAYS + 1):
    hours_of_sleep = float(input(f"Night {day} hours sleep: "))
    while hours_of_sleep < 0 or hours_of_sleep > 24:
        print("Invalid number of hours.")
        hours_of_sleep = float(input(f"Night {day} hours sleep: "))
    total_hours_of_sleep = total_hours_of_sleep + hours_of_sleep 
sleep_debt = recommended_total_sleep_hours - total_hours_of_sleep
print()
print(f"Recommended total sleep is: {recommended_total_sleep_hours}")
print(f"Your total hours of sleep : {total_hours_of_sleep:.2f}")

if sleep_debt > 0:
    print(f"Your sleep debt over this time is: {sleep_debt:.2f}")
else:
    print("You are getting enough sleep. Keep it up!")


