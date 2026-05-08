'''FUNCTIONS 
(1) DEFINE VS CALL
(2) PARAMETR VS ARGUMENT
(3) KEYWORD VS DEFAULT ARGUMENTS 
(4) SCOPES

'''
print("======define vs call =======")
# build in function > print() type()
# Function- reusable block of code!!
# instead of bloc {} in java, python uses indedtation!

# DEFINE- parametr


def greet(a):
    print(f"how do you do? , {a}")


def greeting(b):
    print("greeting is executed")
    return f"hi {b}"


# Call-execute (argument)
result1 = greet('Dina')
print("result1", result1)

result2 = greeting("Aisha")
print("result2:", result2)

print("======PARAMETR VS ARGUMENT=======")

print("======KEYWORD VS DEFAULT ARGUMENTS  =======")
# DEFINE


def give_greet(name, age=22):  # default 22 years old
    print("give_greet is executed")
    return f"hi {name}, you are {age} years old "

# call


result3 = give_greet(name="Dina", age=21)  # keyword argument
print("result3:", result3)

result4 = give_greet("Aisha")  # default argument
print("result4:", result4)


print("======SCOPE =======")
b = 100

# define the function


def calculate(a, b):
    c = a * b
    print(f"the c value: {c}")


# birinchi navbatda block ichidan izlidi, keyib parametrdan , topolmasa tashqaridan izlaydi
# call the function
calculate(5, 50)
