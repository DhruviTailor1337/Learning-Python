# once we created tuple then we cannot change its item

# change the secong item of the list
mytup = ("apple", "ball" , "cat", "dog")
# mytup[1] = "bat"    this will raise error
# print(mytup)

# change the range of item value 
# mytup = ("apple", "ball" , "cat", "dog" , "elephant")
# mytup[0:3] = ("aeroplane", "bat", "cow")        this will raise error
# print(mytup)


# we can convert tuple into list and change list and convert the list back into tuple
mylist = list(mytup)
mylist[0] = ("aeroplane")
mytup = tuple(mylist)
print(mytup)