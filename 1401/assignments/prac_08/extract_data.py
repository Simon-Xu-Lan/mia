"""
record = ["Jimmy", "Smith", (8, 12, 1928), "piano"]

Write code to extract and print specific data, like (sample output):

Last name: Smith
Born: (8, 12, 1928)
Jimmy was born in 1928 and was a great piano player.


Pseudocode:

"""

# record = ["Jimmy", "Smith", (8, 12, 1928), "piano"]
record = ["Wes", "Montgomery", (6, 3, 1923), "guitar"]
print(f"Last name: {record[1]}")
print(f"Born: ({record[2][0]}, {record[2][1]}, {record[2][2]})")
print(f"Jimmy was born in {record[2][2]} and was a great {record[3]} player.")