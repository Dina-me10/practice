'''
OBJECTS 
      whats objects 
      iterabe objects & range 
      dictionary
      error handling systems 

'''

import array  # package/module
import math  # package
from math import ceil
print("======Whats object ==========")
# An object has state and properties
# Everything object in Python

print(type('hello world '))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# paradigma > OOP & functional programming
# OOP 4 concepts > Abstractions, encapculation, inheritance , polimorophism

result1 = math.ceil(97.7)  # call
print("result1", result1)

result2 = ceil(98.7)
print("result2", result2)

print("==========error handling systems ========")

car_dict = dict(name="tayota", year=2026, electric=True)


try:
    print("======================passed here ============")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No speed found", err)
else:
    print("executed succcesfully without error")
finally:
    print("final closing logic")
