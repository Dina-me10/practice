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

print("======= ordinary & static properties =======")

# static state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()

print("===== special/magic methods =====")

# Python's most common special methods are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__ ...


class Car:
    # state
    description = "This class makes cars"

    # special method: __new__
    def __new__(cls, *args):
        print("* __new__ *")
        return super().__new__(cls)

    # constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # methods
    def start_engine(self):
        print(f"The {self.name} started engine!")

    def stop_engine(self):
        print(f"The {self.name} stopped engine!")

    def __str__(self):
        return f"the car.name {self.name} was produced in {self.year} year"

    def __call__(self, ):
        print("object  called as function")
        return True


# create objects
my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("------")

your_car = Car("Toyota", 2026)
print(your_car)
your_car()  # look like function
response = your_car()  # call
print("response", response)
