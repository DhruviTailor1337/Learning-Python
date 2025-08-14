item = input("What item you want to purchase: ")
price = float(input("Enter the price of your item: "))
qty = int(input("Enter quentity you want: "))

total = price*qty

print(f"you have bought {item} and of quentity {qty}. your final price of item is:{total}")
print("Thank you for shopping.")