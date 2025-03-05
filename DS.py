'''#list
letters = ["a","b","c","d"]
matrix = [[1,2,3],["e","f"]]
zeros = [0]*5
print(zeros)
print(zeros + letters)

#list of range
print(list(range(15)))
char = list("engineering")
print(char[::-1])#reverse list
print(len(char))

#accessing elements
letters = ["a","b","c","d"]
print(letters[0:3:2])
numbers = list(range(20))
print(numbers[::2])

#list unpecking
numbers = [1,2,3,4,5,6,8]
first ,second , *other = numbers
print(second,other)

#looping over list
laters = [1,2,3,4,5]
for later in enumerate(laters):
    print(later)

#adding and rremoving item
letters = ["a","b","c","d"]
abc = ["z","y","g"]
letters.append("z")
letters.extend(abc)
letters.insert(2,"t")
print(letters)
print(letters.pop(2))
letters.remove("a")
print(letters)
del letters[0:2]
print(letters)
letters.clear()
print(letters)

#findig item
letters = ["a","b","c","d","e","e","e"]
print(letters.count("e"))
if "e" in letters:
    print(letters.index("e"))

#sorting list
a = [8,56,0,7,87,3]
a.sort()
print(a)
a.sort(reverse = True)
print(a)'''

# lambda function
'''b = lambda a:(1+a)
print(b(12))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))'''

# map function
'''items = [("product1",10),("product2",5),("product3",15)]
# prices = []
# for item in items:
#     prices.append(item[1])

x = list(map(lambda item: item[1],items ))
# for item in x:
#     print(item)
print(x)

fruits = ('apple', 'banana', 'cherry')
x = list(map(lambda fruit: len(fruit),fruits))
print(x)'''

# filter function
'''ages = [5, 12, 17, 18, 24, 32]

#def myFunc(x):
  #if x < 18:
    #return False
  #else:
    #return True

adults = filter(lambda age: age<18, ages)

for age in adults:
  print(age)'''

# list comprehension
'''ages = [(5, 12), (17, 18), (24, 32)]
#[expression for variable in perameter]
x = [age[1] for age in ages]
print(x)'''

# zip function
'''list1 = [1,2,3,4]
list2 = [10,20,30,40]
a = list(zip("abcd",list1,list2))
print(a)'''

# stack -LIFO
'''browsing_sesssion = []
if not browsing_sesssion:
    print("allowed")
browsing_sesssion.append(1)
browsing_sesssion.append(2)
browsing_sesssion.append(3)
# print(browsing_sesssion.pop())
print("redirect", browsing_sesssion[-1])'''

# queues
'''from collections import deque
queue = deque([])
queue.extend([1,2,3,4,5])
for i in range(5):
    queue.popleft()
print(queue)
if not queue:
    print("queue is empty")'''

# swapping variables
'''x = 5
y = 10
# z = x
# x = y
# y = z
x,y = y,x
print(x,y)'''

# Arrays-when large number of lists used
'''from array import array
numbers = array("u",["a","b","c","d","e","f"])
print(numbers[2])'''

# Sets
'''thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
print(len(thisset))
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)'''

# Dictionary
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
'''
# Dicitionary comprehension
''' values = []
# for x in range(5):
#   values.append(x*2)

# [expression for i in items]
values = {x*2 for x in range(5)}
print(values)'''

# generator expression
'''from sys import getsizeof
values = (x*2 for x in range(1000000))
print("gen:",getsizeof(values))'''

# Unpecking operator
'''a = list(range(6))
d = [a,*"hello"]
print(d)'''

