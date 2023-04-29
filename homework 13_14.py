import time
import requests
from bs4 import BeautifulSoup

for x in range(1, 3):
    url = f"https://zoro.to/dubbed-anime?page={x}"
    r = requests.get(url, time.sleep(15))
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