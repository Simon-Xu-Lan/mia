"""
1.Processing Strings
extract just the percentage as a number.
    string = "Result = 95%"
    string = "Final Score = 8%"
    # or
    string = "Relative Value = 178.3%"

Pseudocode:
for each string in the list
    find the positions of "=" and %
    get the number by slicing string using  the above position.
    display the number
"""
# string = "Result = 95%"
# start = string.find("=")
# end = string.find("%")
# print(string[start + 1: end])

# data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
#                 "Something else that's very important = 9.2%", "x = 42%"]
# for each_string in data_strings:
#     start = each_string.find("=")
#     end = each_string.find("%")
#     print(float(each_string[start + 1: end]))


# 2. Date Strings
# Ask the user for their DOB and store it as a string
# Then tell them how old they will be next year
# Remember to think about CONSTANTS for any 'magic numbers' you reuse

# dob = input("DOB: ")
# year = int(dob[-4:])
# age = 2022 - year
# print(f"You were born in {year}")
# print(f"You will turn {age + 1} in 2023.")


# 3.Subject Code Strings
def determine_year_level(subject_code):
    if subject_code[2] == "1":
        year_level = "first-year "
    elif subject_code[2] == "2":
        year_level = "second-year "
    elif subject_code[2] == "3":
        year_level = "third-year "
    elif subject_code[2] == "4":
        year_level = "fourth-year "
    else:
        year_level = "Masters or other "

    return year_level


def determine_subject(subject_code):
    if subject_code[:2] == "CP":
        subject = "IT"
    else:
        subject = ""

    return subject


subject_code = input("Enter subject code: ").upper()
while subject_code != "":
    year_string = determine_year_level(subject_code)
    it_string = determine_subject(subject_code)
    print(f"That is a {year_string}{it_string} subject.")
    subject_code = input("Enter subject code: ").upper()




