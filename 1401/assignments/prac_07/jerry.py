"""
Determine speeding find based on speed input.

Things to note:
The input speed is mph
The speed limit is in kph

Pseudocode
function main
    speed_in_mph = get_valid_number("speed in mph")
    speed_limit_in_kph = get_valid_number("speed limit in kph")
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    fine = determine_fine(speed_in_km, speed_limit_in_kph)
    print fine

function get_valid_number(prompt)
    get speed
    while speed < 0 or speed > 150
        print "invalid input"
        get speed
    return speed

function convert_miles_to_km(speed_in_mph)
    return speed_in_mph * 1.60934

function determine_fine(speed_in_km, speed_limit_in_kph)
    speed_over_limit = speed_in_km - speed_limit_in_kph
    if speed_over_limit < 13
        fine = 177
    else if speed_over_limit <= 20
        fine = 266
    else if speed_over_limit <= 30
        fine = 444
    else if speed_over_limit <= 40
        fine = 622
    else
        find = 1245

    return fine
"""


def main():
    speed_in_mph = float(get_valid_number("speed in mph: "))
    speed_limit_in_kph = float(get_valid_number("speed limit in kph: "))
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    fine = determine_fine(speed_in_kph, speed_limit_in_kph)
    print(fine)


def get_valid_number(prompt):
    speed = float(input(prompt))
    while speed < 0 or speed > 150:
        print
        "invalid input"
        speed = float(input(prompt))
    return speed


def convert_miles_to_km(speed_in_mph):
    return speed_in_mph * 1.60934


def determine_fine(speed_in_km, speed_limit_in_kph):
    speed_over_limit = speed_in_km - speed_limit_in_kph
    if speed_over_limit <= 0:
        fine = 0
    elif speed_over_limit < 13:
        fine = 177
    elif speed_over_limit <= 20:
        fine = 266
    elif speed_over_limit <= 30:
        fine = 444
    elif speed_over_limit <= 40:
        fine = 622
    else:
        fine = 1245

    return fine


# main()


def test_determine_fine():
    speed_limit = 100
    speed = 97
    fine = determine_fine(speed, speed_limit)
    print(f"Speed {speed}km, fine is $0, result is ${fine}")
    speed = 100
    fine = determine_fine(speed, speed_limit)
    print(f"Speed {speed}km, fine is $0, result is ${fine}")
    speed = 105
    fine = determine_fine(speed, speed_limit)
    print(f"Speed {speed}km, fine is $177, result is ${fine}")
    speed = 113
    fine = determine_fine(speed, speed_limit)
    print(f"Speed {speed}km, fine is $266, result is ${fine}")
    speed = 115
    fine = determine_fine(speed, speed_limit)
    print(f"Speed {speed}km, fine is $266, result is ${fine}")
    speed = 120
    fine = determine_fine(speed, speed_limit)
    print(f"Speed {speed}km, fine is $266, result is ${fine}")
    speed = 125
    fine = determine_fine(speed, speed_limit)
    print(f"Speed {speed}km, fine is $444, result is ${fine}")
    speed = 130
    fine = determine_fine(speed, speed_limit)
    print(f"Speed {speed}km, fine is $444, result is ${fine}")
    speed = 135
    fine = determine_fine(speed, speed_limit)
    print(f"Speed {speed}km, fine is $622, result is ${fine}")
    speed = 140
    fine = determine_fine(speed, speed_limit)
    print(f"Speed {speed}km, fine is $622, result is ${fine}")
    speed = 200
    fine = determine_fine(speed, speed_limit)
    print(f"Speed {speed}km, fine is $1245, result is ${fine}")


# test_determine_fine()

