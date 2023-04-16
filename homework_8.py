#სავარჯიშო_1
import sqlite3
base_name = sqlite3.connect("books_db.sqlite")
cursor = base_name.cursor()
cursor.execute("""CREATE TABLE books
(book_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(30),
author VARCHAR(20),
release_year DATE,
price FLOAT);
""")

cursor.execute("""INSERT INTO books(title, author, release_year, price) VALUES("Romeo and Juliet", "William Shakespeare", 1597, 8.88);""")
base_name.commit()

books_list =[
    ("Sherlock Holmes", "Arthur conan Doyle", 1887, 10.45),
    ("Tom Sojer", " Mark Tven", 1876, 7.90),
    ("Harry Potter ", "J.K Rowling", 1997, 12.56),
    ("The Knight in the Panther's Skin", "Shota Rustaveli", 1200, 16.68)
]
cursor.executemany("INSERT INTO books(title, author, release_year, price) VALUES(?,?,?,?)", books_list)
base_name.commit()

base_name.close()



#სავარჯიშო_2
import sqlite3
base_name = sqlite3.connect("titanic.sqlite")
cursor = base_name.cursor()
cursor.execute("""CREATE TABLE passengers
(passenger_id INTEGER PRIMARY KEY AUTOINCREMENT,
passenger_name VARCHAR(20),
age INT,
gender VARCHAR(10),
ticket INT,
cabin INT);
""")

passenger_name = input("enter you name: ")
age = int(input("enter your age: "))
gender = input("enter your gender: ")
ticket = int(input("enter ticket num: "))
cabin = int(input("enter your cabin num: "))

cursor.execute("""INSERT INTO passengers(passenger_name, age, gender, ticket, cabin) VALUES(?,?,?,?,?)""", (passenger_name,age,gender,ticket,cabin))
base_name.commit()

y = []
z =[]
for c in range(3):
    for i in range(5):
        x = input()
        y.append(x)
    z.append(tuple(y))
    y = []

cursor.executemany("INSERT INTO passengers(passenger_name, age, gender, ticket, cabin) VALUES(?,?,?,?,?)", z)
base_name.commit()

base_name.close()


#სავარჯიშო_3
class Movie:
    def __init__(self, title, genre, year, imdb):
        self.title = title
        self.genre = genre
        self.year = year
        self.imdb = imdb

    def __str__(self):
        return f"{self.title}, {self.genre}, {self.year}, {self.imdb}"

movie1 = Movie("Iron man 1", "action/adventure", 2008, 7.9)
movie2 = Movie("Home alone", "comedy", 1990, 7.7)
movie3 = Movie("Harry Potter", "fantasy/adventure", "2001-2010", 7.6)
movie4 = Movie("Titanic", "romance/drama", 1997, 7.9)
movie5 = Movie("The Lion King", "music drama", 1994, 8.5)

import sqlite3
base_name = sqlite3.connect("movies.sqlite")
cursor = base_name.cursor()
cursor.execute("""CREATE TABLE movie
(movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(30),
genre VARCHAR(20),
release_year DATE,
imdb INT);
""")


cursor.execute("INSERT INTO movie(title, genre, release_year, imdb) VALUES(?,?,?,?)",(movie1.title,movie1.genre,movie1.year,movie1.imdb));
base_name.commit()

movie_list = [
    (movie2.title, movie2.genre, movie2.year, movie2.imdb),
    (movie3.title, movie3.genre, movie3.year, movie3.imdb),
    (movie4.title, movie4.genre, movie4.year, movie4.imdb),
    (movie5.title, movie5.genre, movie5.year, movie5.imdb)
]

cursor.executemany("INSERT INTO movie(title, genre, release_year, imdb) VALUES(?,?,?,?)", movie_list)
base_name.commit()

base_name.close()