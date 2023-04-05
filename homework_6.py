#სავარჯიშო_1
class Currency:
    def __init__(self, value, unit="GEL"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value}.00 {self.unit}"

    def changeTo(self, obj):
        if obj == "USD":
            usd = self.value / 2.7
            y = Currency(usd)
            return y.value
        elif obj == "EUR":
            eur = self.value / 3
            y = Currency(eur)
            return y.value
        else:
            return self.value

    def __add__(self, other):
        if other.unit == "USD":
            usd = other.value / 2.7
            a = self.value + usd
            print(f"{a} {self.unit}")
        elif other.unit == "EUR":
            eur = other.value / 3
            a = self.value + eur
            print(f"{a} {self.unit}")
        else:
            a = self.value + other.value
            print(f"{a} {self.unit}")

    def __rmul__(self, other):
        if not isinstance(other, int) and not isinstance(other, float):
            print(TypeError("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე"))
        else:
            print(f"{other * self.value} {self.unit}")

    def __gt__(self, other):
        other.value = other.changeTo(other.unit)
        if other.value > self.value:
            print(f"{other.value} > {self.value}")
        elif other.value < self.value :
            print(f"{other.value} < {self.value}")
        else:
            print(f"{other.value} = {self.value}")



x = Currency(100)
print(x)
print(x.changeTo('USD'))
print(x.changeTo("EUR"))
print(x.changeTo("GEL"))
x2 = Currency(300, "EUR")
x3 = Currency(270, "USD")
x4 = Currency(200, "GEL")
x.__add__(x2)
x.__add__(x3)
x.__add__(x4)
x.__rmul__(7.5)
x.__rmul__(2)
p = 18 * x
x.__rmul__("hi")
x.__gt__(x3)
x.__gt__(x2)
x.__gt__(x4)


#სავარჯიშო_2
class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"name: {self.name}\ndeposit: {self.deposit}\nloan: {self.loan}"

class House:
    def __init__(self, ID, price, owner, status="გასაყიდი"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def sell_house(self, costumer, sesxi=None):
        if sesxi == None:
            x = self.owner.deposit + self.price
            self.status = "გაყიდული"
            print(f"დეპოზიტი- {x}\nსტატუსი- {self.status}\nბინა გაყიდულია")
        else:
            x = self.owner.deposit + self.price
            z = self.owner = costumer
            self.status = "გაყიდულია სესხით"
            y = costumer.loan + sesxi
            print(f"დეპოზიტი- {x}\nსესხის რაოდენობა- {y}\nსტატუსი- {self.status}\nბინა გაყიდულია სესხით\nახლანდელი პატრონის სახელი- {z.name}")


own = Person("Mari")
costumer1 = Person("Nini")
object1 = House("ok", 200, own)
print(own)
print(costumer1)
object1.sell_house(costumer1)
object1.sell_house(costumer1, 300)

#სავარჯიშო_3
class Plane:
    def move(self):
        print("plane can fly")

    def speed(self):
        print("its speed is up to 900km/h")

class Bus:
    def move(self):
        print("bus can move on roads")

    def speed(self):
        print("its speed is up to 180km/h")

def movement(obj):
    obj.move()
    obj.speed()

p = Plane()
p.move()
p.speed()
b = Bus()
b.move()
b.speed()
movement(p)
movement(b)