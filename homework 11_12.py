import sqlite3
import requests
import json

name = input("შეიყვანეთ თქვენი სახელი: ")
print(f"მოგესალმები ძვირფასო მეგობარო {name}, თუ გეოგრაფია არ არის შენი ძლიერი მხარე ნუ შეგეშინდება, ჩვენ გაგიწევთ დახმარებას:)")

con = sqlite3.connect("city.sqlite")
cursor = con.cursor()
api_key = "w1/NljjpwllSTKrxDWZDgA==lNAxnxEnNyipkDn0"

#ამ ცხრილში არის მოცემული ინფორმაცია იმ ქალაქზე რომელიც თქვენ შეიყვანეთ
"""ამ ცხრილს ემატება ინფორმაცია იმ ქალაქზე რომელიც თქვენ შეიყვანეთ"""

cursor.execute("""CREATE TABLE city
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(20),
country VARCHAR(20),
population INT);
""")
x = ""
while x != "no":
    name = input("შეიყვანეთ ქალაქის სახელი: ")
    api_url = f"https://api.api-ninjas.com/v1/city?name={name}"
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
#1
    print(response.status_code)
    print(response.text)
    print(response.headers)
#2
    data = json.loads(response.text)
    json_structure = json.dumps(data, indent=7)
    f = open("json.txt", "w")
    f.write(json_structure)
    f.close()

#3
    city_list = []
    for city in data:
        name = city["name"]
        country = city["country"]
        population = city["population"]

        city_item = {
        "name": name,
        "country": country,
        "population": population
        }

        city_list.append(name)
        city_list.append(country)
        city_list.append(population)

    print("შეყვანილი ქალაქის დასახელება: ", city_item["name"])
    print("შეყვანილი ქალაქის ადგილმდებარეობა: ", city_item["country"])
    print("შეყვანილი ქალაქის მოსახლეობის რაოდენობა: ", city_item["population"])

#4


    cursor.execute("INSERT INTO city(name, country, population) VALUES (?,?,?)", (city_list[0], city_list[1], city_list[2]))
    con.commit()
    x = input("გსურთ დაამატოთ ქალაქი? თუ კი ჩაწერეთ yes, თუ არა no: ")

    if x == "no":
        con.close()
