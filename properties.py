# everything in python is anobject with its properties and method
# class is like an object constructor, or "blueprint" for creating objects
class MyClass():#MyClass is Class
    x = 5

p1 = MyClass()#p1 is object where class called
print(p1.x)#we call method x in p1 object

#__init__() function
#=> it is built in function used to assign values to object properties or other operations that are necessary to do when object is being created.

##Create a class named Person, use the __init__() function to assign values for name and age:
class Person():
    def __init__(self, name, age):
        self.age = age
        self.name = name

p1 = Person("sudhir",23)
print(p1.name, p1.age)

#__str__() function
#=> it controls what should be returned when the class object is represented as string.
#=> if __str__() function is not set the string representation of the object is returned
class Person():
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("sudhir",23)
print(p1)

##create a method in class person:

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def MyFunc(self):
        print("hello! My name is " + self.name)
        print(f"My age is {self.age}")

p1 = Person("sudhir", 23)
p1.age = 40
p1.MyFunc()

# The self perameter is the current instance of the class and it is used to access variables that belong to the class.
# it does not have to be named self you can call it whatever you like , but it has to be the first perameter of any function in the class.
class Person():
    def __init__(mysillyobj , name, age):
        mysillyobj.name = name
        mysillyobj.age = age

    def myfunc(abc):
        print("hii! i am "+ abc.name)

p1 = Person("vinay",23)
p1.myfunc()

#class definition can not be empty but if you have a class DEFINITION WITHOUT CONTENT for some reason put the pass statement to avoi getting an error.
# class Book:
#     pass

##INHERITENCE##
#=> inheritence allows us to define a class that inherits all the methods and properties from another class.
#=> parent class is the class being inherited from ,also called base class.
#=> child class is the class that inherits from another class, also called derived class

##Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self,f_name,surname):
        self.f_name = f_name
        self.surname = surname
    
    def printname(self):
        print(self.f_name, self.surname)

class Student(Person):
    pass

p1 = Student("krishna","vora")
# p1.surname = "vala" #for change in surname or veriable
p1.printname()

# if we add __init__() function to child class it will no longer inherit the __init__() function of perant class

## the chld's __init__() overrides he inhertence of the perant's __init__() function.
class Person:
    def __init__(self,fname,surname):
        self.fname = fname
        self.surname = surname
    
    def printname(self):
        print(self.fname, self.surname)

class Student(Person):
    def __init__(self , fname, surname):
        Person.__init__(self, fname, surname)
    def mark(self):
        print("90 marks achieved by "+ self.fname)


p1 = Student("krishna","vora")
# p1.surname = "vala" #for change in surname or veriable
p1.printname()
p1.mark()


#we can also use super() function that will make the child class to inherit all the methods and properties from its perant.
# class Student(Person):
#     def __init__(self, fname, surname):
#         super().__init__(fname, surname)

class Person:
    def __init__(self, fname , surname):
        self.fname = fname
        self.surname = surname

    def printname(self):
        print(self.fname , self.surname)
        

class Student(Person):

    def __init__(self, fname , surname):
        super().__init__(fname , surname)
        self.gradyear = 2019 

    def grad(self):
        print("i did my graduation in",self.gradyear)

p1 = Student("nia","shetty")
p1.printname()
p1.grad()
