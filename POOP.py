class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        print(f"{self.name} can walk well")
    def speak(self):
        print(f"{self.name} can speak well")

Person1 = Person("Kevin Obunga", 29, "male")
Person2 = Person("Mercy", "20","Female" )

print(Person1.name)
print(Person1.age)
print(Person1.gender)

Person1.walk()
Person1.speak()

Person2 = Person("Mercy", "20","Female" )

print(Person2.name)
print(Person2.age)
print(Person2.gender)

Person2.walk()
Person2.speak()