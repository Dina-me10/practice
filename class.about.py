print("=======CLASS =========")
# class - blueprint for object creation...
# structure > state constructor method


class Person:  # class definition
    # static state property (class variable)
    message = "class state property"

    # constructor (special method)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ordinary instance method
    def introduce(self):
        print(f"{self.name} says: how do u do?")

    def say_age(self):
        print(f"{self.name} says: I am {self.age}")

    # class method
    @classmethod
    def explain(cls):
        print("class method property executes:")


# create instances
person1 = Person("Justin", 25)
person2 = Person("Martin", 25)
person3 = Person("John", 25)

# ordinary state
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()

print("=======ordinary & static properties =========")
# static state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()
