# in python if we want to access item, we have to use indexing
# the first item in list have index 0, second item have index 1, and it goes on...


# positive indexing
mylist = ["apple", "ball", "cat", "dog"]
print("First item:",mylist[0])          #returns First item: apple
print("last item: ",mylist[3])          #returns Last item: dog


# negative indexing
print("last item: ",mylist[-1])
print("Second item: ",mylist[-3])

# explanation:  0     1     2     3
#             apple  ball  cat   dog
#              -4     -3    -2   -1


# range of indexing
print("1st three item:",mylist[0:3])
print("last three items using positive index:",mylist[1:])
print("last three item using negative index:",mylist[-3:])