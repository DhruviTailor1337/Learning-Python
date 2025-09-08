operator = input("Enter operator (+ - * /):")
num1 = float(input("Enter 1st Number:"))
num2 = float(input("Enter 2nd Number:"))

if operator == "+":
    result = num1 + num2
    print("sum:",result)

elif operator == "-":
    result = num1 - num2
    print("subtraction:",result)

elif operator == "*":
    result = num1 * num2
    print("multiplication:",result)

elif operator == "/":
    result = num1 / num2
    print("division:",result)

else:
    print(f"{operator} is not valid!")