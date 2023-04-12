#სავარჯიშო_1
import sqlite3
base_name = sqlite3.connect("books_db.sqlite")
cursor = base_name.cursor()
cursor.execute("""CREATE TABLE books
(book_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR,
author VARCHAR,
release_year DATE,
price FLOAT);
""")

cursor.execute("""INSERT INTO books(title, author, release_year, price) VALUES("Romeo and Juliet", "william shakespeare", 1597, 8.88);""")
base_name.commit()

books_list =[
    ("sherlock holmes", "arthur conan doyle", 1887, 10.45),
    ("tom sojer", " mark tven", 1876, 7.90),
    ("Harry Potter ", "j.k rowling", 1997, 12.56),
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
passenger_name VARCHAR,
age INT,
gender VARCHAR,
ticket INT,
cabin INT);
""")

passenger_name = input("enter you name: ")
age = int(input("enter your age: "))
gender = input("enter your gender: ")
ticket = int(input("enter: "))
cabin = int(input("enter your cabin num: "))

cursor.execute("""INSERT INTO passengers(passenger_name, age, gender, ticket, cabin) VALUES(?,?,?,?,?)""", (passenger_name,age,gender,ticket,cabin))
base_name.commit()

passengers_list =[
    (input(), input(), input(), input(), input()),
    (input(), input(), input(), input(), input()),
    (input(), input(), input(), input(), input())
]
cursor.executemany('INSERT INTO passengers(passenger_name, age, gender, ticket, cabin) VALUES(?,?,?,?,?)', passengers_list)
base_name.commit()

base_name.close()


#სავარჯიშო_3
class Movie:
    def __init__(self, title, genre, year, imdb):
        self.title = title
        self.genre =genre
        self.year = year
        self.imdb = imdb

    def __str__(self):
        return f"{self.title}, {self.genre}, {self.year}, {self.imdb}"

import sqlite3
base_name = sqlite3.connect("movies.sqlite")
cursor = base_name.cursor()
cursor.execute("""CREATE TABLE movie
(movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR,
genre VARCHAR,
year DATE,
imdb INT);
""")

movie1 = Movie("Iron man", "hero", 2009, 23)
cursor.execute("""INSERT INTO movie(title, genre, year, imdb) VALUES(movie1.title, movie1.genre, movie1.year, movie1.imdb);""")
base_name.commit()

movie_list = [
    Movie("Iron man", "hero", 2009, 23),
    Movie("Iron man", "hero", 2009, 23),
    Movie("Iron man", "hero", 2009, 23),
    Movie("Iron man", "hero", 2009, 23)
]

cursor.executemany('INSERT INTO movie(title, genre, year, imdb) VALUES(?,?,?,?)', movie_list)
base_name.commit()

base_name.close()