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
