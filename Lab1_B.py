def main():

    price = float(input("Enter the price of the item: "))
    tax = float(input("Enter the sales tax percentage: "))
    total = price + (price * (tax/100))

    print(f'Your total is ${total:.2f}')

main()
