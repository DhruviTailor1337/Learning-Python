age = int(input("enter age:"))
if age <= 5:
    print("ticket is free for kids.")
elif age <= 12:
    print("ticket price: ₹100")
elif age <= 18:
    print("ticket price: ₹150")
elif age <= 60:
    print("ticket price: ₹300")
else:
    print("ticket price (senior citizen): ₹130")