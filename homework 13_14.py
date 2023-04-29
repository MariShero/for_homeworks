import time
import requests
from bs4 import BeautifulSoup


dub_sub = input("what kind of anime do you want to watch DUBBED or SUBBED: ")
url = f"https://zoro.to/{dub_sub}-anime"
r = requests.get(url, time.sleep(15))
# print(r.status_code) ვამოწმებთ დავუკავშირდით თუ არა სერვერს
content = r.text
soup = BeautifulSoup(content, "html.parser")
body = soup.find("body")
wrapper = body.find("div", id="wrapper")
main_wrap = wrapper.find("div", {"class": "layout-page"})
container = main_wrap.find_all("div", {"class": "container"})[1]
main_content = container.find("div", id="main-content")
block_area = main_content.find("section", {"class":"block_area block_area_category"})
tab = block_area.find("div",{"class": "tab-content"})
film_list = tab.find("div", {"class": "film_list-wrap"})
flw_item = film_list.find_all("div", {"class": "flw-item"})

for i in flw_item:
    film_detail2 = i.find("div", {"class": "film-detail"})
    text1 = film_detail2.a.text
    print(text1)

    file = open("anime.csv", "a", encoding="utf-8")
    file.write(text1)
    file.write("\n")
    file.close()
#რექვესთებს შორის ხანგრძლივობა, 15-20 წმ