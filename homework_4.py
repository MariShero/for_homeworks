#სავარჯიშო_1
class People:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        print(f"{self.firstname}.{self.lastname}.school@edu.ge")

class Lecturer(People):
    def __init__(self, firstname,lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_email(self):
        print(f"{self.firstname}.{self.lastname}@edu.ge")

class Student(People):
    def __init__(self,firstname, lastname, courses = []):
        super().__init__(firstname, lastname)
        self.courses = courses

    def get_email(self):
        print(f"{self.firstname}.{self.lastname}.1@edu.ge")


p1 = People("Tony", "Stark")
p2 = Lecturer("Nini", "Kvinikadze", 500)
p3 = Student("Mariam", "Sherozia", ["IT", "english", "basketball"])
p1.get_email()
p2.get_email()
p3.get_email()


#სავარჯიშო_2
class Libraryitem:
    def __init__(self, title, subject, status = "available" or "occupied"):
        self.title = title
        self.subject = subject
        self.status =status

    def booking(self):
        if self.status == "available":
            print("ეს ნივთი ხელმისაწვდომია, თქვენ შეგიძლიათ მისი გატანა")
        elif self.status == "occupied":
            print("ვწუხვართ მაგრამ ამ საგნის დაჯავშნა შეუძლებელია")

class Book(Libraryitem):
    def __init__(self, title, subject, status, ISBN, authors):
        super().__init__(title, subject, status)
        self.ISBN =ISBN
        self.authors = authors

class Magazine(Libraryitem):
    def __init__(self, title, subject, status, volume, journalname):
        super().__init__(title, subject, status)
        self.volume =volume
        self.journalName = journalname

class CD(Libraryitem):
    def __int__(self, title, subject, status):
        super().__init__(title, subject, status)

x = Book("ვეფხისტყაოსანი", "ქართული", "available", "?", "შოთა რუსთაველი")
x1 = Magazine("Spider man", "?", "available", "?", "spider man")
del x1.title
del x1.subject
x2 = CD("dance monkey", "?", "occupied")
del x2.subject
x.booking()
x1.booking()
x2.booking()


#სავარჯიშო_3
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname =firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"hi, i'm person"

class Employee:
    def __init__(self, profession, monthly_salary, working_hours):
        self.profession = profession
        self.salary = monthly_salary
        self.hours = working_hours

    def hourly_salary(self):
        return self.salary / self.hours

class Doctor(Person, Employee):
    def __init__(self, firstname, lastname, age, profession, monthly_salary, working_hours):
        Person.__init__(self, firstname, lastname, age)
        Employee.__init__(self, profession, monthly_salary, working_hours)

    def perform_operation(self):
        return f"თქვენი გაჭრის დროა, არ შეგეშინდეთ ოპერაციისას თირკმელს არავინ მოგპარავთ"

p1 = Doctor("მარიამ", "შეროზია", 15, "ქირურგი", 2000, 20)
print(p1)
print(p1.hourly_salary())
print(p1.perform_operation())