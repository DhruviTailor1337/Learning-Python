#create a long string and replace 4 char
#in python we cannot change the original string 
#therefore we fisrt create original string and then do changes in other string
str1="welcome to dhruvitailor1337"
str2="W" + str1[1:8] + "T" + str1[9:11] + "D" + str1[12:17] + "T" + str1[18:]
print(str2)