print("===== INHERITANCE =====")
# PARENT > CHILD
# parent only provides public/protected properties to their children


class Animal:  # Parent
    # state
    description = "The class parent for animals"

    # constructor
    def __init__(self, voice):
        self._status = "this animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


class Cat(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def plays(self):
        print(f'the cat {self.name} loves to play with various games')

    def voiceEatting(self):
        print(f'{self.name} make {self.sound} while eating')


class Horse(Animal):
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def plays(self):
        print(f"The horse {self.name} loves to gallop and play in the fields.")

    def voiceEatting(self):
        print(f"{self.name} makes a soft {self.sound} while eating hay.")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
horse = Horse("Noor", "hihihi", True)


dog.introduce()
cat.introduce()
horse.introduce()

print("---------")

dog.make_voice()
cat.make_voice()
horse.make_voice()


print("---------")
print(Animal.description)


print('dog status:', dog._status)
print('cat status:', cat._status)
print('horse status:', horse._status)
