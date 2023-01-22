
# Julie is planning a holiday and wants to record all the places she goes in the order she visits them.
# Once she returns, she wants to be able to display the list of places and also which place had the longest name (because she likes that sort of thing).

# Peseudocode:
# places = empty list
# get place
# while place is not empty
#     add place to places
#     get place
# for place in places
#     print place


# code
places = []
longest_place = ""
place = input("Place: ").title()
while place != "":
    places.append(place)
    place = input("Place: ").title()
if len(places) == 0:
    print("I went nowhere :(")
else:
    print("On my holiday, I went to: ")
    for place in places:
        print(place)
        if len(place) > len(longest_place):
            longest_place = place
    print(f"The place with the longest name was {longest_place}")