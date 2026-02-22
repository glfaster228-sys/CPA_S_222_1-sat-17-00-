class Cat:
    def __init__(self, name, age, fur_color, breed):    
        self.name = name
        self.age = age
        self.fur_color = fur_color
        self.breed = breed
    def meow(self):
        return f"{self.name} says: Meow!"
class Dog:
    def __init__(self, name, age, fur_color, breed):
        self.name = name
        self.age = age
        self.fur_color = fur_color
        self.breed = breed
    def bark(self):
        return f"{self.name} says: Woof!"