#Exercise 2 (shopping cart program)

Item = input("what Item would you like to buy?: ")
price = float(input("what is the price of the item?: "))
quantity = int(input("How many are you buying?: "))
total = price * quantity

print(f"the total price of the items in your cart is: {total}")