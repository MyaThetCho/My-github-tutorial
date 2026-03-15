quantity = int(input("Enter total textbook : "))
if quantity>=1 and quantity<=5:
    cost = 20
    price = quantity*20
elif quantity>=6 and quantity<=9:
    cost = 15
    price = quantity*15
else:
    cost = 12
    price = quantity*12


print("\t \t Invoice")
print("-"*45)
print("Quantity \t \t Price per Book($)")
print("-"*45)
print(quantity, "\t \t \t", cost)
print("-"*45)
print("Total \t \t \t", price)