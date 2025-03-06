# exception is kind of error that terminates the program execution
numbers = [1,2]
print(numbers[3])

age = int(input("age:"))

# handling exeption
try:
    age = int(input("age:"))

except ValueError:
    print("you didn't enter valid age")

print("execution continuous")

try:
    age = int(input("age:"))
    xfactor = 10/age

except ValueError:
    print("you didn't enter valid age")
except ZeroDivisionError:
    print("age cannot be zero")
else:
    print(" no exception were thrown ")

# cleaning up
try:
    file = open("exception.py")
    age = int(input("age:"))
    xfactor = 10/age
except ValueError:
    print("you didn't enter valid age")
except ZeroDivisionError:
    print("age cannot be zero")
else:
    print(" no exception were thrown ")
finally:
    file.close()

# with statement
try:
    with open("exception.py") as file, open("another.txt") as target:
        print("file opened")
        # file.__exit__
    age = int(input("age:"))
    xfactor = 10/age
except ValueError:
    print("you didn't enter valid age")
except ZeroDivisionError:
    print("age cannot be zero")
else:
    print(" no exception were thrown ")
finally:
    file.close()

# raise exception
def calculate(age):
    if age<=0:
        raise ValueError("age cannot be 0 or less")
    return age/10
try:
    calculate(-2)
except ValueError as error:
    print(error)

from timeit import timeit

code1 = "" 
def calculate(age):
    if age<=0:
        raise ValueError("age cannot be 0 or less")
    return age/10
try:
    calculate(-2)
except ValueError as error:
    print(error)
    pass
""
print("first code=",timeit(code1, number=1000))