'''
Array & set 
(1) array
(2)set 
(3)specific operators with set
'''

from array import array
print("==========array =========")

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

print("========set============")
# set of unique collection without keeping order!
new_numbers = array("1", 1, 4, 5, 7, 8, 41)
numbs_set = set(new_numbers)

print(f" the numbs_set: {numbs_set} and type: {type(numbs_set)}")

numbs_set.add(200)
print("numbs_set(1):", numbs_set)

numbs_set.add(7)
print("numbs_set(2):", numbs_set)

print("==========specific operators==============")
# |, &, -, ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union
result2 = a & b  # intersection
result3 = a - b  # difference
result4 = a ^ b  # symmetric difference
print("Union", result1)
print("Intersection", result2)
print("Difference", result3)
print("Symmetric difference", result4)
