'''
comprehension
(1) what is comprehension / list comp
(2) set and dictionary comp
'''
print("===========what is comprehension / list comp ")
# Comprehension acts like a spread operator

''' Comprehension general syntax:
A) * itarable
B) <expression> for item in iterable
C) <expression> for item in iterable <condition>
'''
# LIST COMP
numbers = [1, 4, 3, 2, 1, 20]
list_numbers = [*numbers]  # version


print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))


people = [
    ("Aisha", 20),
    ("Dina", 21),
    ("Mery", 30),
]
list_people = [person[0] for person in people]  # b version
print("list_people:", list_people)


cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33),
]
list_cars = [car[0] for car in cars if car[1] > 70]
print("list_cars:", list_cars)

print("=======set and dictionary comp====")
numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}
print("SET_numbs:", set_numbs)


dict_people = {person[0]: person[1] for person in people}
print("dict_people:", dict_people)

dict_people2 = {person[0] for person in people if person[1] > 20}  # condition
print("dict_people2:", dict_people2)
