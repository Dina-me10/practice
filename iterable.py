# takrorlanish hususiyatiga ega
print("=======iterable objects & range  =======")
# iterable objects & dicts tuplelist range map filter

range_obj = range(3)
print("range_obj:", range_obj)
text = "MIT"
for letter in text:
    print(f"letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")


print("======= Dictionary =======")
# dictionary is json object :

person = {"name": "dina", "age": 21, "single": True, "hobby": "cycling"}
person_obj = dict(name="dina", age=25, single=True, hobby="cycling")

print(f"The person: {person}")
print(f"The person_obj: {person_obj}")

'''name = person_obj["name"]
print("name:", name)

hobby = person_obj["hobby"]
print("hobby:", hobby)
'''
# method: get()
name = person_obj.get("name")
major = person_obj.get("major", "IT")
balance = person_obj.get("balance", 0)
print(f" the name : {name}, major: {major}  and balance: {balance}")

del person_obj["single"]
for key in person_obj:
    print(f"the key: {key} => value {person_obj[key]}")
