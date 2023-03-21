#სავარჯიშო_1
class Celsius:

    def __init__(self, temperature):
        self.__temperature = temperature

    def get_temp(self):
        return self.__temperature

    def set_temp(self, new_temp):
        self.__temperature = new_temp

    def del_temp(self):
        del self.__temperature

    temperature = property(get_temp, set_temp, del_temp)

ce1 = Celsius(40)
ce2 = Celsius(18)
print(ce1.temperature)
ce1.temperature = 55
print(ce1.temperature)
print(ce2.temperature)
ce2.temperature = 78
print(ce2.temperature)

#სავარჯიშო_2
class Bank_Account:
    def __init__(self, account_name, balance=0):
        self.__account_name = account_name
        self.__balance = balance

    def __str__(self):
        return f"გამარჯობა {self.__account_name}, თქვენ ანგარიშზე გაქვთ {self.__balance} ლარი"

    def get_name(self):
        return self.__account_name

    def set_name(self, new_name):
        self.__account_name = new_name

    def deposit(self):
        amount = int(input(f"{self.__account_name}, შეიყვანეთ თანხა რომლის დამატებაც გსურთ ანგარიშზე: "))
        self.__balance += amount
        print("თანხის შეტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ ", amount, "ლარი")

    def withdraw(self):
        amount = int(input(f"{self.__account_name}, შეიყვანეთ თანხა რომლის გამოტანაც გსურთ ანგარიშიდან: "))
        if amount > self.__balance:
            print("თქვენს ანგარიშზე არ გაქვთ ამ რაოდენობის თანხა")
        else:
            self.__balance -= amount
            print("თანხის გამოტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ ", self.__balance, "ლარი")


bal1 = Bank_Account("Mariam")
print(bal1)
bal1.deposit()
bal1.withdraw()

#სავარჯიშო_3
from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y =y

    def distance(self):
        return sqrt(self.x**2 + self.y**2)

point1 = Point(3, 5)
point2 = Point(6, 9)
print(point1.distance())
print(point2.distance())

# ბონუს_დავალება
""""ეს ვცადე მაგრამ ვერ დავასრულე"""
# class Fraction:
#
#     def __init__(self, top, bottom):
#         self.top = int(top)
#         self.bottom = int(bottom)
#
#     def add(self, x):
#         if self.bottom ==x.bottom:
#             self.top += self.top
#         else:
#             self.top = self.top*self.bottom+self.bottom+x.top
#             self.bottom = self.bottom+x.bottom
#
#     def display(self):
#         print(str(self.top) + "/" + str(self.bottom))
#
# nam = Fraction(2, 7)
# nam1 = Fraction(4, 7)
# nam.display()
# nam1.display()
# print(nam.add(nam1))

