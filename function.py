#definig function
def greet(f_name,surename):
    print(f"hi {f_name} {surename}")
    print("welcome to abroad")
greet("nidhi","koria")


# two types of function
#1- perform the task
#2- reeturns the value
def get_greeting(name):
    return (f"hi {name}")

message = get_greeting("nidhi")
file = open("content.txt","w")
file.write(message)
#increament function
def increament(number,by):
    return number + by

#result = increament(3,1)
#print(result)
print(increament(3,4))

#default arguments
def increament(number,by = 1):
    return number + by

#result = increament(3,1)
#print(result)
print(increament(3))


#use of xargs
def multiply(*numbers):
    print(list(numbers))

multiply(1,2,3,4,20)

def multiply(*numbers):
    total = 1
    for number in numbers:
        total*= number
        return total
print(multiply(9,2,3,40,5))

#xxargs
def save_user(**user):
    print(user["id"])

save_user(id=1,name="nidhi",course="abc")

#global variable
message = "a"
def greet(name):
    global message
    message = "b"

greet("nidhi")
print(message)

# exercise
def fizz_buzz(input):
    if input % 3 ==0:
        return "fizz"
    elif input % 5 ==0:
        return "buzz"
    else:
        return "fizz_buzz"

result = fizz_buzz(2)
print(result)
    





