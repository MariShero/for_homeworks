import time

import requests
from bs4 import BeautifulSoup

url = "https://www.webtoons.com/en/top"
r = requests.get(url, time.sleep(15))
# print(r.status_code) ვამოწმებთ დავუკავშირდით თუ არა სერვერს
content = r.text
soup = BeautifulSoup(content, "html.parser")
body = soup.find("body", {"class": "en"})
wrap = body.find("div", id="wrap")
container = wrap.find("div", id="container")
content = container.find("div", id="content")
p_wrap = container.find("div", {"class": "popular_wrap"})
ranking = p_wrap.find("div", {"class": "ranking_lst popular NE=a:tnt"})
type = ranking.find("ul", {"class": "lst_type1"})
li = type.find_all("li")
for i in li:
    info = i.find("div", {"class": "info_area"})
    subj = info.find("p",{"class": "subj"})
    text = subj.text
    print(text)

    file = open("manga.csv", "a", encoding="utf-8")
    file.write(text)
    file.write("\n")
    file.close()

