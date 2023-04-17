
import sqlite3
base_name = sqlite3.connect("customers.sqlite")
base_name.row_factory = sqlite3.Row
cursor = base_name.cursor()
result = cursor.execute("SELECT * FROM users")
for row in result:
    print(row["username"], row["phone_number"])
result = cursor.execute("SELECT * FROM users WHERE age > 25")
for row in result:
    print(row["firstname"], row["lastname"], row["age"])
age = 25
result = cursor.execute("SELECT * FROM users WHERE age > :age_condition", {"age_condition": age})
for row in result:
    print(row["firstname"], row["lastname"], row["age"])

result = cursor.execute("SELECT * FROM users WHERE age BETWEEN 10 AND 25")
for row in result:
    print(tuple(row))
result = cursor.execute("SELECT * FROM users WHERE age <> 20")
for row in result:
    print(row["firstname"], row["lastname"])
result = cursor.execute("SELECT count(user_id) FROM users")
for row in result:
    list(row)
    print(row[0])

result = cursor.execute("SELECT * FROM users order by age desc ")
for row in result:
    print(tuple(row))

result = cursor.execute("SELECT DISTINCT firstname FROM users order by firstname")
for row in result:
    print(tuple(row))

result = cursor.execute("UPDATE users SET username='Mari' WHERE age = 20")
print(cursor.rowcount)
base_name.commit()

result = cursor.execute("UPDATE users SET age = 15 WHERE age > 30")
print(cursor.rowcount)
base_name.commit()

result = cursor.execute("DELETE FROM users WHERE user_id = 5")
print(cursor.rowcount)
base_name.commit()

result = cursor.execute("DELETE FROM users WHERE firstname LIKE 'ა%'")
print(cursor.rowcount)
base_name.commit()

base_name.close()


