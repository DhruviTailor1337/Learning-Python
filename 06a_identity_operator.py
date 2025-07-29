# identity operator refers to check if two values are located at the same memory location
# we use "is" and "is not"

# IMP -> having two variable with equal value doesn't neccesary mean to they are identical

a = 10
b = 10

c = "Dhruvi"
d = "Dhruvi"

e = [1, 2, 3]
f = [1, 2, 3]

print(a is b)        # True
print(a is not b)    # False

print(c is d)        # True
print(c is not d)    # False

print(e is f)        # False
print(e is not f)    # True
# here e is not b because the interpreter locates the value of list seperately in memory
# although they are equal. 