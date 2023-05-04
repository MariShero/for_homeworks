#1
import sqlite3
conn = sqlite3.connect("survey.sqlite")
cursor = conn.cursor()

result = cursor.execute("SELECT count(id) FROM students where SelfStudyHour <2")
for row in result:
    list(row)
    print(row[0])

def amount(device, age):
    result = cursor.execute("SELECT count(id) FROM students WHERE Device = ? AND Age = ?",(device, age))
    for row in result:
        list(row)
        print(row[0])

x = amount("Smartphone", 20)

cursor.execute("""INSERT INTO students(Age, OnlineClassTime, Device, SelfStudyHour, FitnessTime, Sleep, SocialMedia, SocialMediaPlatform) VALUES(15, 2, "Laptop", 3, 1, 9, 3, "youtube");""")
conn.commit()

result = cursor.execute("""UPDATE students SET SocialMediaPlatform = "MARIAM-gram" WHERE Age <> 21""")
conn.commit()

conn.close()

#2
import json

file = open("sample.json", "r+")
data = json.load(file)

print(data["person"]["address"])

x = data["person"]["friends"]
z = []
for i in range(len(x)):
    z.append(data["person"]["friends"][i]["name"])
print(z)

a = data["person"]
for i in a:
    p = input("შეიყვანეთ ველის დასახელება: ")
    if p == i:
        print(data["person"][p])
        break
    elif p != i:
        print("თქვენი შეყვანილი ველის სახელი არასწორია გთხოვთ შტანოთ თავიდან")
file.close()