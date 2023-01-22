"""
Transfer and display a series of number of seconds into minutes and seconds

Pseudocode:

function main()
    for i from 0 to 6
        seconds = i * 635
        minutes_seconds_str = transfer_sec_to_min_sec(seconds)
        print minutes_seconds_str

function transfer_sec_to_min_sec(seconds)
    min = seconds // 60
    sec = seconds % 60
    return minutes_seconds_str
"""


def main():
    for i in range(6):
        number_of_seconds = i * 635
        format_str = "{number_of_seconds} seconds is {minutes}m {seconds}s"
        minutes_seconds_str = build_min_sec_str(number_of_seconds, format_str)
        print(minutes_seconds_str)

    seconds_you_love = int(input("Favourite duration in seconds: "))
    format_str = "You love {minutes}m {seconds}s"
    print(build_min_sec_str(seconds_you_love, format_str))



def build_min_sec_str(number_of_seconds, format_str):
    min = number_of_seconds // 60
    sec = number_of_seconds % 60
    minutes_seconds_str = format_str.format(
        number_of_seconds=number_of_seconds,
        minutes=min,
        seconds=sec
    )

    return minutes_seconds_str


main()