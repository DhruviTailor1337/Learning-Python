class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"hyy i am {self.name} and my age is {self.age}")
    
    def sound(self):
        print(f"meow")

class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"hyy my name is {self.name} and age is {self.age}")
    
    def sound(self):
        print('bark')

cat1 = cat('kitty',5)
dog1 = dog('toffy',4)

for animal in(cat1,dog1):
    animal.sound()
    animal.intro()
    animal.sound()
    
