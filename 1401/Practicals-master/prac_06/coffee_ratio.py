"""1. Coffee Brew Ratio"""

# ===Algorithm===
# get dose, yield
# ratio = yield / dose
# print ratio

def main():
    dose = get_valid_number("Dose: ", 0.1, 100)
    coffee_yield = get_valid_number("Yield: ", 0.1, 100)
    ratio = coffee_yield / dose
    style = determine_coffee_style(ratio)
    print(f"1 : {ratio} is considered {style}")

# Determine coffee style
# if ratio is from 1:1 to a 1:2 then “ristretto”
# else if ratio is from 1:2 to a 1:3 ratio then “normale”
# else if ratio is from 1:3 to a 1:4 ratio then“lungo”
def determine_coffee_style(ratio):
    if ratio < 2:
        style = "ristretto"
    elif ratio < 3:
        style = "normale"
    else: 
        style = "lungo"  
    
    return style

def check_coffee():
    style = determine_coffee_style(0.1)
    print(style)  # This should be ristretto
    style = determine_coffee_style(1)
    print(style)  # This should be ristretto
    style = determine_coffee_style(1.5)
    print(style)  # This should be ristretto
    style = determine_coffee_style(2)
    print(style)  # This should be normale
    style = determine_coffee_style(2.5)
    print(style)  # This should be normale
    style = determine_coffee_style(3)
    print(style)  # This should be lungo
    style = determine_coffee_style(3.5)
    print(style)  # This should be lungo
    style = determine_coffee_style(4)
    print(style)  # This should be lungo
    style = determine_coffee_style(13.5)
    print(style)  # This should be lungo

def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number

# check_coffee()
main()

