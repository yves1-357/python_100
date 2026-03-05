class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def methode(self):
        print("Hello my name is ")

p1 = Person("John", "36")
p1.methode()
print(f"{p1.name} {p1.age}")