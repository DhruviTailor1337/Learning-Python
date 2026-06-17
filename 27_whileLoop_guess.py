secret = 44
i = 0
while i!= secret:
    i = int(input('guess: '))
    print("wrong")
    if i<secret:
        print('too low')
    elif i>secret:
        print('to high')
print('correct!!')