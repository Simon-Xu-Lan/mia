print("Menu:", "(I)nstructions", "(C)alculate", "(Q)uit", sep="\n")
choice = input("Choice: ").upper()
is_continue = True
while is_continue:
    if choice == "I":
        print("Enter the number of products you want to buy and your chosen price.")
        print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
        print("Menu:", "(I)nstructions", "(C)alculate", "(Q)uit", sep="\n")
        choice = input("Choice: ").upper()
    elif choice == "C":
        number_of_products = int(input("Number of products: "))
        while number_of_products < 0:
            print("Invalid input")
            number_of_products = int(input("Number of products: "))
        price = float(input("Price: "))
        if number_of_products <=5:
            total_price = number_of_products * price 
        else:
            total_price = number_of_products * price * 0.9
        print(f"{number_of_products} x ${price} products = ${total_price:.2f}")
        print("Menu:", "(I)nstructions", "(C)alculate", "(Q)uit", sep="\n")
        choice = input("Choice: ").upper()
    elif choice == "Q":
        is_continue = False
        print("Farewell")
    else:
        print("Invalid choice")
        print("Menu:", "(I)nstructions", "(C)alculate", "(Q)uit", sep="\n")
        choice = input("Choice: ").upper()

