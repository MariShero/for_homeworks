# სავარჯიშო_1
class Rectangle:
    """"გამოიყენება მართკუთხედის ფართობისა და პერიმეტრის გასაგებად"""

    def __init__(self, width, length, color):
        self.sigane = width
        self.simagle = length
        self.peri = color

    def perimeter(self):
        return 2 * (self.sigane + self.simagle)

    def area(self):
        return self.simagle * self.sigane

obj1 = Rectangle(1, 5, "blue")
obj2 = Rectangle(3, 3, "green")
obj3 = Rectangle(3, 7, "puple")
print(obj1.area())


#სავარჯიშო_2
class Car:

    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"მანქანის ბრენდი {self.brand}, მანქანის მოდელი {self.model}, მანქანის ფერი {self.color}"

car1 = Car("Red", "Ford", "Mustang")
print(car1)
car2 = Car("Blue", "Toyota", "Prius")
print(car2)
car3 = Car("Green", "Volkswagen", "Golf")
print(car3)

#სავარჯიშო_3
class Dog:

    def __init__(self, breed="Neapolitan mastiff", size="large", age="5 years", color="black"):
        self.breed = breed
        self.size = size
        self. age = age
        self.color = color

    def sleep(self):
        return f"{self.age} - მცირე ასაკის გამო მათ დიდხანს ძინავთ"
    def eat(self):
        return f"{self.size} ზომა მიუთითებს რომ მათაც ლექციაზე ჩემსავით უყვართ ჭამა"
    def run(self):
        return f"{self.breed} ჯიშის ძაღლი საკმაოდ ათლეტურია"

dog1 = Dog()
dog2 = Dog("Maltese", "small", "2 years", "white")
dog3 = Dog("Chow chow", "midium", "3 years", "brown")
print(dog2.sleep())
print(dog1.eat())
print(dog3.run())

