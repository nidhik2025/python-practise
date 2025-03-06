# class-blueprint for creating new object
# object-instance of a class
# class: human
# object: jhon,jeck,mery,nia,jully

# creating class
class Point:
    def draw(self):
        print("draw")

point = Point()
print(type(point))
print(isinstance(point, Point))

# constructor
class Point:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        print(f"Point ({self.x},{self.y})")

point = Point(100,2)
print(point.default_color)
# print(point.x)
point.draw()

another = Point(10,30)
another.draw()
# print(type(point))
# print(isinstance(point, Point))

# class and instance method
class Point:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @classmethod #decorator - to extend the behaviour of the function
    def zero(cls):
        cls(0,0)
    def draw(self):
        print(f"Point ({self.x},{self.y})")

point = Point(100,2)
print(point.default_color)
# print(point.x)
point.draw()

another = Point(10,30)
another.draw()
# print(type(point))
# print(isinstance(point, Point))

class stud:
    def __init__(self,a,b):
        self.x = a
        self.y = b
    def __eq__(self, abn):
        return self.x == abn.x and self.y == abn.y

    def __str__(self):
        return f"({self.x},{self.y})"
        
stn = stud(2,3)
abn = stud(2,3)
print(stn==abn)


# coustom containers
 





