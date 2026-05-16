''' 
list 
(1)working with lists 
(2) list methods 
(3) lambda function
(4) enumarate, map and filter

'''
print("=== working with lists ===")
# java/php/ nodejs array  => python list
# literal
person = {"name": "Aisha", "age": 20}  # /dictinary
people = ("Aisha ", "Dina", "Mery")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the TEAM: {team}")

# constructor
result = list("Hello world!")
print(f"the result: {result} and the size is {len(result)}")

print("✅"*20)

fruits = ["apple", "banana", "orange", "kiwi", "lemon"]

a = fruits[0]
b = fruits[0:2]  # [0, 2)
c = fruits[::3]
d = fruits[::-1]

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")

print('=== list methods ===')
print("✅"*20)
# Methods: append(), insert(), pop(), remove(), clear(), sort() - these are mutable methods
# index()

letters = ["a", "b", "c", "d"]
letters.append("e")
print(f"APPEND result: {letters}")  # append adds behind

names = ["Dina", "Aisha", "Alex", "John"]
# usage: input index, element. This puts any element to the shown index
names.insert(2, "Jonh")
print(f"INSERT result: {names}")

cars = ["BMW", "Rolsroys", "Genesis", "Kia"]
size = len(cars) - 1
output = cars.pop(size)  # pops the element
print(f"POP result: {output} is removed and remain cars are: {cars}")

animals = ["cat", "dog", "horse"]
animals.pop(0)  # pop removes a element of shown index from the list
print(f"POP 2: {animals}")

phones = ["Iphone", "Samsung", "Galaxy"]
print(phones)
phones.remove("Galaxy")  # removes from the list
print(f"REMOVE result: {phones}")

del phones[1]  # deletes an element of the shown index from the list
print(f"DELETE operator executed {phones}")

exist = cars.index("Rolsroys")  # check the index
print(exist)

phones.clear()  # clears phones list
print(f"CLEAR result: {phones}")

if "Iphone" in phones:
    print(f"the Iphone's index is: {phones.index("Iphone")}")
else:
    print("Iphone doesn't exist anymore")

numbers = [2, 20, 12, 5, 3, 9]
numbers.sort()
print(f"SORT result: {numbers}")
numbers.sort(reverse=True)
print(f"SORT with REVERSE result {numbers}")


# sorted() function - this works almost like sort but it is immutable
numbs = [2, 1, 100, 4, 7, 8]
sort_numbs = sorted(numbs)
print(f"the numbs: {numbs} and sorted numbs {sort_numbs}")

print("=== lambda function ===")
print("✅"*20)
# lambda is small anonim function


def calculate(a, b): return a * b


result = calculate(3, 5)
print(result)

people = [
    ("Aisha", 20),
    ("Dina", 21),
    ("Alex", 25),
    ("Mery", 30)
]

people.sort()
print(f'Case 1: {people}')

people.sort(key=lambda person: person[1])
print(f"Case 2: {people}")
