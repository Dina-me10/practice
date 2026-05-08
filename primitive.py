print("==========")
# in Java, variable name of storage location
# in Python , varibale is named reference

count = 100
count_type = type(count)

print(f"the count: {count} and type {count_type}")

result1 = count.bit_count()  # method

result2 = count.numerator  # state
print(result1, result2)


print("===== strings ======")
# METHODS: upper() lower() title() find() replace()

course = "Ai Python fullstack"
result = type(course)
print(f"the result (1) {result}")
result = course.title()
print(f"the result:(2) {result}")

result = course.upper()
print(f"the result:(3) {result}")

result = course.replace("fullstack", "MasterClass")
print(f"the result:(3) {result}")


print("===== booleans ======")
# functions> type() input() bool() int() str()
y = input("give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")

# TRUTHY VS FALSY value
# truthy > true 100 -100 "MIT"
# falsy> false 0 "" none

test_falsy = ""
print("the_falsy:", bool(test_falsy))

test_truthy = "MIT"
print("the_truthy:", bool(test_truthy))
