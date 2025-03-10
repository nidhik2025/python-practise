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
# arithmatic operation
class std:
    def __init__(self,a ,b):
        self.a = a
        self.b = b

    def __add__(self,other):
        return std(self.a + other.a, self.b + other.b)
    
s1 = std(10,20)
s2 = std(5,6)
sum = s1 + s2
print((sum.a,sum.b))
    
# coustom containers
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self,tag):
        self.tags[tag] = self.tags.get(tag,0)+1

cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
# counting of iteration
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self,tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0)+1
    
    def __getitem__(self, tag):
        self.tags.get(tag.lower(), 0)

    # def __setitem__(self,key,value)
    def __setitem__(self,tag,count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)
    
    def __iter__(self):
        return  iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)

#properties
class math:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    