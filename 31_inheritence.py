# Single Inheritance	            One parent → One child
#  Multiple Inheritance	            Multiple parents → One child
#  Multilevel Inheritance	        Grandparent → Parent → Child
#  Hierarchical Inheritance	        One parent → Multiple children
#  Hybrid Inheritance	            Combination of two or more inheritance types

#single inheritence(animal->dog)
class animal:
    def eat(self):
        print('animal can eat')

class dog(animal):
    def bark(self):
        print('dog can bark')
obj1 = dog()
obj1.eat()
obj1.bark()

print('==============================')

#single inheritence(person->student)
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f'person name:{self.name} and age:{self.age}')

class student(person):
    def __init__(self, name, age,course):
        super().__init__(name, age)
        self.course = course
    def show_student(self):
        print(f'course:{self.course}')

stu1 = student('dhruvi',20,'Msc.IT')
stu1.display()
stu1.show_student()

print('==============================')

#Multilevel Inheritance (Vehicle → Car → ElectricCar)
class vehicle:
    def start(self):
        print("vehical starts")
    
class car(vehicle):
    def drive(self):
        print('car is driving')

class electricCar(car):
    def charge(self):
        print('bettery is charging')

tesla = electricCar()

tesla.start()
tesla.drive()
tesla.charge()


print('==============================')


# Multiple Inheritance
class mother:
    def cook(self):
        print('mother loves cooking')

class father:
    def drive(self):
        print('father loves driving')

class daughter(mother,father):
    def study(self):
        print('dhruvi loves study')

obj1 = daughter()
obj1.cook()
obj1.drive()
obj1.study()



print('==============================')


# Hierarchical Inheritance
class employee:
    def work(self):
        print('employee is working')
class manager(employee):
    def manage_team(self):
        print('manager is manage team')
class developer(employee):
    def write_code(self):
        print('developer is writing the code')
        
manager1 = manager()
developer1 = developer()

manager1.work()
manager1.manage_team()

developer1.work()
developer1.write_code()