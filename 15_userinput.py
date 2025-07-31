# if we want to get input from user then we simply use input() method

name=input("Enter your Name:")
print("hello ",name)


# all user input are of type String. if want other input type then simpli we have to
# write that perticular data_type before the input() method (like type casting)

# ask for number
num=input("Enter any number:")
print("you entered:",num)
print("data-type of the number before type casting:",type(num))

num=int(num)
print("data-type of the number After type casting:",type(num))