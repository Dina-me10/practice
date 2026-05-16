'''
TUPLE
(1)WHATS TUPLE , TUPLE VS LIST
(2) ORDINARY VS STATIC PROPERTIES 
(3)ZIP 

'''
print('=== tuples vs list  ===')


'''
list vs tuple:
tuple qiymatlarini o'zgartirib bo'lmaydi (immutable)!
'''
# literal
num = [1, 3, 5, 7]

# konstruktor (matndan ro'yxat yasash)
letters = list('Salom dunyo!')

fruits = ["olma", "banan", "kivi", "limon"]
print(f"{fruits}")

const = fruits[0]
print(const)
fruits[2] = "qovun"
print(fruits)

# tuplelar o'zgarmasdir
animal = ("yo'lbars", "maymun", "eshak", "it")
tuple_obj = ("MIT", 2026, True)

print(animal[0])  # Birinchi elementni ko'rish

print(animal)
