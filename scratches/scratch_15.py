name = str(input("Enter the name: "))
price = float(input("Price: "))
print("Original price was ", price)

if name[0] =='H':
    if name[1] == 'e' and price >= 1000:
        if name[2] == 'r' and price >= 500 and price < 5000:
            amount = price - 300
            print("Discount price is ", amount)
            print("You saved 300.0")
        elif price >= 5000:
            amount = price - 500
            print("Discount price is ", amount)
            print("You saved 500.0")
        else:

            amount = price - 110
            print("Discount price is ", amount)
            print("You saved 110.0")
    else:

        amount = price - 110
        print("Discount price is ", amount)
        print("You saved 110.0")

else:
    print("Discount price is ", price)
    print("You saved 0.0")






