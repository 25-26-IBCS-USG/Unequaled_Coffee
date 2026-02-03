# Coffee Shop

def main():
    price = 0
    order = ""
    print("Welcome to CS Cafe!")
    print(" 1. Cappuchino - $4.30 \n 2. Macchiato - $5.00 \n 3. Espresso - $2.50 \n 4. Mocha - $4.80 \n 5. Latte - $5.20")
    response = input("What would you like to order?")
    while True:
        if response == ("1"):
            price = price + 4.30
            order = order + "Cappuchino, "
        if response == ("2"):
            price = price + 5.00
            order = order + "Macchiato, "
        if response == ("3"):
            price = price + 2.50
            order = order + "Espresso, "
        if response == ("4"):
            price = price + 4.80
            order = order + "Mocha, "
        if response == ("5"):
            price = price + 5.20
            order = order + "Latte, "
        response = input("Anything else?")
        if response == ("No"):
            break

    print("Your total order is "+ str(order) + "for "+ str(price) + " dollars")


        
if __name__ == "__main__":
    main()

