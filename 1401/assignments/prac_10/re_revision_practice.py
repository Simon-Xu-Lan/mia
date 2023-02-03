# Input, Processing, Output
def calculate(number, percent):
    return number * (1 + percent)


original = float(input("Original: "))
change = float(input("Change: "))
result = calculate(original, change)
print(f"Original: {original}, Change: {change}, Result: {result}")


# Decision Structures
# 2
hour_count_after_noon = 0
hours = []
hour = int(input("The time of day (0-23): "))
while hour >= 0:
    hours.append(hour)
    if hour >= 12:
        hour_count_after_noon += 1
    hour = int(input("The time of day (0-23): "))
print(hours)
print(f"{hour_count_after_noon} hours were after noon.")


# 3. Coffee orders made simple.
def calculate_cost(color, size):
    if size == "small":
        cost = 3
    elif size == "medium":
        cost = 4
    else:
        cost = 5

    if color != "black":
        cost += 1
    return cost


color = input("White or black coffee: ").lower()
size = input("Small, Medium, or Large: ").lower()
cost = calculate_cost(color, size)
print(f"You coffee costs ${cost}.")



# Repetition Structures
numbers = []
low_value = int(input("Low value: "))
high_value = int(input("High value: "))
for number in range(low_value, high_value + 1):
    numbers.append(number)
print(f"{numbers} totals: {sum(numbers)}")