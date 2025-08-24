# you cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

mySet = {"Dhruvi","Tailor",1337}
for i in mySet:
    print(i)        #this output can unordered because set not followed indexing rule


# if you want to check if specific item is present or not
print("Dhruvi" in mySet)         #True
print("Tailor" not in mySet)     #false


