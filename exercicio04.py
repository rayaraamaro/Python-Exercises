class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says woof!"
    

class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says meow!"
    
max = Dog("Max")
raj = Cat("Raj")

print(max.speak())
print(raj.speak())

for pet in [max,raj]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet): #Função para chamar qualquer uma das duas classes
    print(pet.speak())

pet_speak(max)
pet_speak(raj)

class Bee():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says zzzz"

class Fish():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says gluglu"

lis = Bee("Lis")
lula = Fish("Lula")

print(lis.speak())
print(lula.speak())
