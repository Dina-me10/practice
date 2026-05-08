print("==========")
# in Java, variable name of storage location
# in Python , varibale is named reference

count = 100
count_type = type(count)

print(f"the count: {count} and type {count_type}")

result1 = count.bit_count()  # method

result2 = count.numerator  # state
print(result1, result2)
