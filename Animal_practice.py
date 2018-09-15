class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display(self):
        print (self.name, self.health)
# a = Animal("dog", 150)
# a.walk().display()

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150

# c = Animal("dog")
# c.display()
c = Dog("dog")
c.display()