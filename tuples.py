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

print(animal[0])

print(animal)

print("=== Argumentlarni yoyish (Unpacking) ===")

groups = ["MIT", "Flexy", "Devex", "MG"]
# Unpacking: x va y birinchi ikkita qiymatni oladi, *z esa qolganlarini ro'yxatga yig'adi
(x, y, *z) = groups
print(f"z ga qolgan barcha elementlar tushdi: {z}")


def calculate(*args):
    # *args - istalgancha sondagi oddiy argumentlarni qabul qiladi (tuple ko'rinishida)
    print("*args (kelgan sonlar):", args)
    total = 1
    for x in args:
        total *= x
    print(f"umumiy natija: {total}")
    return total


# Turli xil sondagi argumentlar bilan chaqiramiz
calculate(1, 7, 4, 5)
print('--------------')
calculate(0, 2, 300)
print('--------------')
calculate(5, 7)
