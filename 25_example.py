age = int(input("Enter your age:"))
duration = int(input("How many minuts do you exercise per day?: "))

if age < 18:
    print("Do light sports and fun activities.")

elif age <= 40:
    if duration >= 30:
        print("Intermediate workout plan recommended.")
    else:
        print("Start with beginner 15-min routines.")
else:
    print("Focus on low impact workouts like yoga or walking.")