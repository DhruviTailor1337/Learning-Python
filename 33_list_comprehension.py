# list comprehension -> concise way to create a new list based on the values of an existing list.
# double the list value
list = [1,2,3,4,5]
doubled_list = [i*2 for i in list]
print(doubled_list)


# ===========for Loop vs. List Comprehension==========
# List comprehension makes the code cleaner and more concise than for loop.
#for loop:
num = [1,2,3,4,5]
square_num = []
for i in num:
    square_num.append(i*i)
print(square_num)


#using list comprehension
mynum = [1,2,3,4,5]
square_mynum = [i**2 for i in mynum]
print(square_mynum)


# ========Conditionals in List Comprehension===========
# List comprehensions can utilize conditional statements like if…else to filter existing lists.
even_num = [i for i in range(1,11) if i%2 == 0 ]
print("even num:",even_num)

odd_num = [i for i in range(1,10) if i%2 != 0]
print("odd num:",odd_num)



# ============List Comprehension with String===============
str1 = "elephant"
vowels = "aeiou"
result = [char for char in str1 if char in vowels]
print(result)

