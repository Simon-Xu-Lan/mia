# 1. Print a line
def print_a_line():
    """prints a line of 40 hyphens."""
    print(40 * "-")

def question_1():
    """test funciton print_a_line"""
    print_a_line()

# 2. Is it even?
def is_even(number):
    """determine if an integer is even"""
    return number % 2 == 0


def question_2():
    """test function is_even"""
    some_number = int(input("Number: "))
    if is_even(some_number):
        print(f"{some_number} is even")
    else:
        print(f"{some_number} is odd")


# 3. Get Non-empty String
def get_string(prompt):
    """get a non-empty string"""
    str = input(f"{prompt}: ")
    while len(str) == 0:
        str = input(f"{prompt}: ")
    return str

def question_3():
    name = get_string("Name")
    birthplace = get_string("Birth place")
    print(f"Hi {name} from {birthplace}")

# 4. Number List
def get_min_max():
    min = int(input("Minimum number: "))
    max = int(input("Maximum number: "))
    while max <= min:
        print(f"Your maximum must be greater than {min}")
        max = int(input("Maximum number: "))
    return min, max

def question_4():
    min, max = get_min_max()
    a_list = []
    for num in range(min, max + 1):
        a_list.append(num)
    print(a_list)


# 5. Subject List
def is_letter(str):
    result = True
    for char in str:
        result = result and char.isalpha()
    return result

def is_number(str):
    result = True
    for char in str:
        result = result and char.isdigit()
    return result


def is_valid(code):
    if len(code) != 6:
        return False
    elif not is_letter(code[:2].lower()):
        return False
    elif not is_number(code[2:]):
        return False
    else:
        return True


def question_5():
    subjects = []
    code = input("Enter subject code: ")
    while len(code) != 0:
        if not is_valid(code):
            print("Invalid subject code")
        else:
            subjects.append(code.upper())
        code = input("Enter subject code: ")
    print(f"You do have these {len(subjects)} subjects")
    for subject in subjects:
        print(subject)
    print("You are cool")



def main():
    question_5()

main()

