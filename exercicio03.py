class Animal():
    def __init__(self):
        print("Animal Created")
    
    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal): #Classe derivada
    def __init__(self):
        Animal.__init__(self)
        print ("Dog Created")

    def eat(self):
        print("I am a dog and eating")

    def bark(self):
        print("WOOF!")

myanimal= Animal()
mydog = Dog()
mydog.eat()
