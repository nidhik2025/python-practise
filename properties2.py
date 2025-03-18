##ITERATORS:
#=>iterator is an object that contains a countable number of values
#=> an iterator is an object that can be iterated upon, meaning that you can traverse all the values.
#=> it implements the iterator protocal which consist of the methods __iter__() and __next__()

# all the objects have iter() method to get an iterator
'''fruit = ("apple","banana","strawberry","pineapple","kiwi","mango")
fruit1 = "cherry"
myshope = iter(fruit1)

# print(next(myshope))
# print(next(myshope))
# print(next(myshope))
# print(next(myshope))
# print(next(myshope))
for x in fruit:
    print(x)#looping 

for y in fruit1:
    print(y)  

# to create an object/class as an iterator we have to implement the methods __iter__() and __next__() to your object.
# __iter__() method also use to do operation but must be always return the iterator object itself.
# __next__() method also do operation and must return the next item in the sequence.

##Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class Num:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a+=1
        return x
    
mynum = Num()
myit = iter(mynum)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
for i in range(5):
    print(next(myit))
#use of Stopiteration 
class Num:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a+=1
            return x 
        else:
            raise StopIteration

mynum = Num()
myit = iter(mynum)
for x in myit:
    print(x)


##POLYMORPHISM:
#=> it refers to the many form of methods/functions/operators with same name that can be executed in many objects or classes
# FUNCTION POLYMORPHISM:
# => a function that can be used for different objects len() function
x = "Mathematic power" #string
print(len(x))
x = ("Mathematics","Physics", "Chemistry",) #tuple
print(len(x))
abcd = {
    "mathematcs" : 67,
    "physics" : 89,
    "chemistry" : 90,
    "sanskrit" : 77,
    "english" : 59
}
print(len(abcd))

##CLASS POLYMORPHISM
#=> if there is multiple class with the same method name it is called polymorphism
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class car(Vehicle):
    
    def move(self):
        print("drive!")

class Boat(Vehicle):
    def move(self):
        print("sail!")

class Plane(Vehicle):
    def move(self):
        print("fly!!")        

car1 = car("ford",123)
boat1 = Boat("ibiza", "A26")
plane1 = Plane("boeing","F2G78")    

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
'''

