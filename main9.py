class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def start_engine(self):
        return f"The {self.make} {self.model}'s engine has started."
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def drive_car(self, car):
        return f"{self.name} is driving the {car.make} {car.model}."
my_car = Car("Toyota", "Prado")
person = Person("Asif", 19)
print(person.drive_car(my_car))
    