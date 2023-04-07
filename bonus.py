#სავარჯიშო_1
from math import sqrt
class Point:
    def __init__(self):
        self.x = int(input("enter x: "))
        self.y = int(input("enter y: "))

    def __str__(self):
        return f"{self.x},{self.y}"

    def __add__(self, other):
        distance = (other.x - self.x)**2 + (other.y - self.y)**2
        return sqrt(distance)

a = Point()
b = Point()
print(a)
print(b)
print(a.__add__(b))

#სავარჯიშო_2
class Stairs:
    def __init__(self, n):
        self.n = n

    def climbstairs(self):
        last_step = 1
        step = 1
        for i in range(self.n - 1):
            last_step_cope = last_step
            last_step += step
            step = last_step_cope
        print(f"სულ არსებობს {self.n} კიბეზე ასვლის {last_step} გზა")


stair = Stairs(5)
stair.climbstairs()

#სავარჯიშო_3
class Roman:
    def Romen_to_Intenger(self, s):
        x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        y = 0
        for i in range(len(s)):
            if i > 0 and x[s[i]] > x[s[i - 1]]:
                y += x[s[i]] - 2 * x[s[i - 1]]
            else:
                y += x[s[i]]
        return y


print(Roman().Romen_to_Intenger('MCDLXXIV'))



#სავარჯიშო_4
class Vector:
    def __init__(self, x, y):
        self.x = x
        self. y = y

    def __add__(self, other):
        x1 = self.x + other.x
        y1 = self.y + other.y
        new = Vector(x1, y1)
        return f"{new.x},{new.y}"

    def __mul__(self, other):
        if not isinstance(other, int):
            print(TypeError("მოცემული თანამამრავლი არ გახლავთ მთელი რიცხვი"))
        else:
            x2 = self.x * other
            y2 = self.y * other
            new1 = Vector(x2, y2)
            return f"{new1.x},{new1.y}"

    __rmul__ = __mul__


a = Vector(5, 7)
b = Vector(7, 9)
print(a.__add__(b))
print(a.__mul__(2))
b.__mul__("hi")
c = 2 * a
print(c)
