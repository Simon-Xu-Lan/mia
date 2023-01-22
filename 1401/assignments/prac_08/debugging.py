"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
# names = ["Abby", "Jerome", "Olivia", "Monique"]
# print("My friends' names: ")
# for i in range(1, len(names)):
#     print(f"{i}. {names[i]}")
# last_number = len(names)
# print(f"The last name (number {last_number}) is {names[last_number]}")

# Problem(s) for program 1:
# ?
# "list index out of range" in the following code
# print(f"The last name (number {last_number}) is {names[last_number]}")
# Fixed code for program 1:
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(1, len(names)):
    print(f"{i}. {names[i]}")
last_number = len(names) - 1
print(f"The last name (number {last_number}) is {names[last_number]}")

# Debug program 2 - title-casing country names
# countries = ("australia", "new zeaLAND", "India")
# for i in range(len(countries)):
#     countries[i] = countries[i].title()
# print(countries)  # country names should be in title-case now

# Problem(s) for program 2:
# ?
# TypeError: 'tuple' object does not support item assignment
# The program tried to modify element in tuple.

# Fixed code for program 2:
countries = ["australia", "new zeaLAND", "India"]
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now