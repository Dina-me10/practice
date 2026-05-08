# dunder _builtins_, _init_
message = "Python: Everything is object"
print(message)

result = type(message)
print("result:", result)

''' In Python there are builtin tools:
(1) Types: int float str list dict
(2) Function: print() len() input() type() str() int()
(3) Constants: true false none 

'''

print(dir(__builtins__))
