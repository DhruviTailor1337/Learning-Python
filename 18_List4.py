# List methods

#------------- add list item--------------------
# append()
mylist = ["apple", "ball" , "cat", "dog"]
mylist.append("elephant")
print(mylist)

# insert()   -->insert item at specific index
mylist.insert(1,"bat")
print(mylist)

# extend()
list2 = ["fish","girl","hourse"]
mylist.extend(list2)
print(mylist)


# --------------remove list item----------------
# remove() -->removes specified item
mylist.remove("cat")
print(mylist)

# pop()  -->removes specified index
mylist.pop(1)
print(mylist)

# if you not specified any index then it removes last item
mylist.pop()
print(mylist)

# clear()   -->empties the list
mylist.clear()
print(mylist)


# --------------sort list----------------------
list3 = ["b", "d", "e", "o", "a" ]
list3.sort()
print(list3)

list_num = [9,4,7,2,7,3]
list_num.sort()
print(list_num)

# -----------------descending list-------------
list3.sort(reverse=True)
print(list3)


# -----------------reverse list----------------
list3.reverse()
print(list3)

# -----------------copy a list------------------
list4 = list3.copy()
print(list4)
# or use slice operator
list5 = list3[:]
print(list5)


# ------------------join lists-------------------
list6 = list2+list5
print(list6)