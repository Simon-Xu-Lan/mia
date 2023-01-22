"""
Question:
Write a complete Python program that ask the user for quantity of random numbers
and a maximum, then generates and store that many numbers between 0 and the
maximum. When you've got this part working, add the following interesting additions:
- minimum
- maximum
- random choice from existing list (Hint: if there are 7 numbers it will be a number at a random index 0-6)
- the list reversed*
- the list sorted*

Pseudocode:
numbers = empty list
get quantity of random numbers
get maximum
for i in range of quantity of random numbers
    use randint(0, maximum) to generate a random number
    add the random number to numbers
print numbers
print minimum of numbers
print max of numbers
pirnt a number in numbers by random index
print reversed list
print sorted list
"""

# Code
import random
numbers = []
quantity = int(input("How many random numbers: "))
maximum = int(input("Maximum number: "))
for i in range(quantity):
    random_number = random.randint(0, maximum)
    numbers.append(random_number)
print(f"The numbers are: {numbers}")
print(f"The minimum is {min(numbers)}")
print(f"The maximum is {max(numbers)}")
random_index = random.randint(0, len(numbers) - 1)
print(f"A randomly chosen number is {numbers[random_index]}")
numbers.reverse()
print(f"The numbers reversed are {numbers}")
numbers.sort()
print(f"The numbers sorted are {numbers}")

