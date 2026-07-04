#simple function
def myFunct1():
    print("Hello")
myFunct1()

# function with 1 argument
def myFunct2(name):
    print(name)
myFunct2("Dhruvi")

# functon with 2 argument
def myFunct3(age,rollNum):
    print("your age is:",age)
    print("your roll number is:",rollNum)
myFunct3(19,44)

#function with default argument
def myFunct4(rollNum,age=20):       #the non default arguments always comes first
    print(f'your age is:{age} and roll number is {rollNum}')

myFunct4(44)


#keyword arguments
def myfunct5(rollnum,age):
    print(f"your roll number is {rollnum} and age is {age}")
myfunct5(age=25,rollnum=44)


#lambda function to find square
square = lambda x:x**2
print(square(5))

#lambda function to find even odd
check = lambda x: 'even' if x%2==0 else 'odd'
print(check(5))
