#list
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
print(a)