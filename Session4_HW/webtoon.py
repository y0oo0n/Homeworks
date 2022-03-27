import requests
from bs4 import BeautifulSoup

MON_URL = f"https://comic.naver.com/webtoon/weekdayList?week=mon"
mon_html = requests.get(MON_URL)
mon_soup = BeautifulSoup(mon_html.text,"html.parser")

mon_list_box = mon_soup.find("ul",{"class":"img_list"})
mon_list = mon_list_box.find_all("li")

def extract_info(mon_list):
    result = []

    for mon in mon_list:
        title = mon.find("dt").find("a").string
        author = mon.find("dd",{"class":"desc"}).find("a").text
        rating = mon.find("div",{"class":"rating_type"}).find("strong").text

        mon_info = {
            'title': title,
            'author': author,
            'rating': rating,
        }

        result.append(mon_info)

    return result