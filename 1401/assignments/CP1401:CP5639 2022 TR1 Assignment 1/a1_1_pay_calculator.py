"""
CP1401 2022-2 Assignment 1
Program 1 - Pay Calculator
Student Name: Mei Zhong
Date Started:

Pseudocode:
BASE_PAY = 45
display "Experience Counts Pay Calculator"
get number_of_hours_worked, experience_level
hourly_pay = BASE_PAY * (1 + 0.05 * expericence_level)
total_pay = hourly_pay * number_of_hours_worked
display hourly_pay, total_pay 
"""

BASE_PAY = 45
print("Experience Counts Pay Calculator")
number_of_hours_worked = int(input("Number of hours worked: "))
experience_level = int(input("      Experience level: "))
hourly_pay = BASE_PAY * (1 + 0.05 * experience_level)
total_pay = hourly_pay * number_of_hours_worked
print(f"Based on your experience level ({experience_level}):")
print(f"Your hourly pay rate is ${hourly_pay:.2f}")
print(f"Your total pay is ${total_pay:.2f}")


