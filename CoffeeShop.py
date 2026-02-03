# Coffee Shop

def main():
    price = 0
    print("Welcome to CS Cafe!")
    while True:
        print(" 1. Cappuchino - $4.30 \n 2. Macchiato - $5.00 \n 3. Espresso - $2.50 \n 4. Mocha - $4.80 \n 5. Latte - $5.20")

        response = input("What would you like to order?")

        if response == ("1"):
            price = price + 4.30
        if response == ("2"):
            price = price + 5.00
        if response == ("3"):
            price = price + 2.50
        if response == ("4"):
            price = price + 4.80
        if response == ("5"):
            price = price + 5.20
        response = input("Anything else?")
        if response == ("No"):
            break
if __name__ == "__main__":
    main()
