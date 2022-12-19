"""4. Add Functions to Previous Pracs"""
# Calculate salary for worker level

def main():
    worker_level = get_invalid_number("Worker lever: ", 1, 10)
    salary = calculate_salary(worker_level)
    print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")

def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number

def calculate_salary(level):
    salary = 5000 * level
    return salary


# main()


# Print grid

def main():
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
    print_grid(rows, columns)

def print_grid(rows, columns):
    for row in range(rows):
        print("*" * columns)


# main()