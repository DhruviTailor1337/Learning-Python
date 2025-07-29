# there are two type of conversion
# 1-> implicit conversion (automatic)
# 2-> explicit conversion (manual)

# example of implicit convertion
int_num = 44
print(type(int_num))

float_num = 1.2
print(type(float_num))

new_num = int_num + float_num
print("sum:", new_num)
print(type(new_num))


print("\n")
# explicit conversion(also known as type casting)
# example--> addition of string and integer
num_string = "12"
print("type of num_string before conversion",type(num_string))

num_int = 23
# print("sum:", num_string + num_int )

# but if we want to add this two number then we have to convert num_string into int
num_string = int(num_string)
print("type of num_string after conversion:", type(num_string))

num_sum = num_string + num_int
print("sum:", num_sum)
print("datatype of num_sum:",type(num_sum))