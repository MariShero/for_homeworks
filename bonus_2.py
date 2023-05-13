#davaleba_1
class Illness:
    def __init__(self, ID, name):
        self.id = ID
        self.name = name

    def __str__(self):
        return f"თქვენი id- {self.id}, დაავადების სახელია- {self.name}"

class Doctor:
    def __init__(self, name_surname, department):
        self.name_surname = name_surname
        self.department = department
        self.patient_list = []

class Patient:
    def __init__(self, personal_number, patient_name, doctor):
        self.personal_number = personal_number
        self.pat_name = patient_name
        self.ill_name = []
        self.doc = doctor

    def __str__(self):
        return f"პაციენტის პირადობა - {self.personal_number}, პაციენტის სახელი- {self.pat_name}, ექიმის სახელი- {self.doc} დაავადების სახელი- {self.ill_name}"

    def diagnose(self, illness, doctor=None):
        if doctor == None:
            return f"თქვენი დაავადების სახელია: {illness.name}"
        else:
            self.ill_name.append(illness.name)
            if len(doctor.patient_list) < 20:
                self.doc = doctor.name_surname
                doctor.patient_list.append(self.pat_name)
            else:
                print("ექიმის მიმაგრება ვერ მოხდება")
            return self.ill_name, self.doc, doctor.patient_list


ill = Illness(2, "Corona")
doc = Doctor("anastasia", 18)
pat = Patient(123, "mari", doc.name_surname)
print(ill)
print(pat)
print(pat.diagnose(ill, doc))
print(pat.diagnose(ill))



#davaleba_2
import sqlite3
import requests
from bs4 import BeautifulSoup

con = sqlite3.connect("Crypto.sqlite")
con.row_factory = sqlite3.Row
cursor = con.cursor()
cursor.execute("""CREATE TABLE cryptoMarket(
id INTEGER PRIMARY KEY AUTOINCREMENT,
Title VARCHAR(30),
Name VARCHAR(30),
Price INT,
Change INT,
Per_Change INT,
MarketCap INT);
""")

url ="https://finance.yahoo.com/crypto/?guccounter=1"
r = requests.get(url)
print(r.status_code)

content = r.text
soup = BeautifulSoup(content, "html.parser")
body = soup.find("body")
app = body.find("div", id="app")
data = app.find("div")
d = data.find("div")
render = d.find("div", {"class": "render-target-active render-target-default Pos(a) W(100%)"})
bgc = render.find("div", {"class": "Bgc($bg-body) Mih(100%) W(100%) Bgc($layoutBgColor)! finance US"})
lead = bgc.find("div", id="YDC-Lead")
lead1 = lead.find("div", id="YDC-Lead-Stack")
lead2 = lead1.find("div", id="YDC-Lead-Stack-Composite")
d1 = lead2.find("div", id="mrt-node-Lead-5-ScreenerResults")
proxy = d1.find("div", id="Lead-5-ScreenerResults-Proxy")
screener = proxy.find("section", id="screener-results")
fin = screener.find("div", id="fin-scr-res-table")
pos = fin.find("div", id="scr-res-table")
ovx = pos.find("table", {"class": "W(100%)"})
tbody = ovx.find("tbody")
tr = tbody.find_all("tr")
for i in tr:
    tds = i.find_all("td")
    title = tds[0].find("a").text
    name = tds[1].text
    price = tds[2].text
    change = tds[3].text
    per_change = tds[4].text
    market_cap = tds[5].text

    cursor.execute("INSERT INTO cryptoMarket(Title, Name, Price, Change, Per_Change, MarketCap)VALUES(?,?,?,?,?,?)", (title, name, price, change, per_change, market_cap));
    con.commit()


x = cursor.execute("SELECT * FROM cryptoMarket")
z = {}
for row in x:
    dic = {row["Title"]: {
        "name": row["Name"],
        "price": row["Price"],
        "change": row["Change"],
        "%change": row["Per_Change"],
        "market cap": row["MarketCap"]
    }}
    z.update(dic)

print("მთლიანი ინფორმაცია:", z)