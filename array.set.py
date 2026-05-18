'''
Array & set 
(1) array
(2)set 
(3)specific operators with set
'''
from array import array

numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers(1):", numbers)

numbers.append(100)
numbers.insert(0, 14)
print("numbers(2):", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(3)", numbers)

del numbers[0:2]
print("numbers(4)", numbers)
