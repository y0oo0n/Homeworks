import requests
from bs4 import BeautifulSoup
from webtoon import extract_info
import csv

file = open('webtoon_mon.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","author","rating"])


MON_URL = f"https://comic.naver.com/webtoon/weekdayList?week=mon"
mon_html = requests.get(MON_URL)
mon_soup = BeautifulSoup(mon_html.text,"html.parser")

mon_list_box = mon_soup.find("ul",{"class":"img_list"})
mon_list = mon_list_box.find_all("li")

monday_list = []
monday_list += extract_info(mon_list)


for result in monday_list:
    row=[]
    row.append(result['title'])
    row.append(result['author'])
    row.append(result['rating'])
    writer.writerow(row)

print(monday_list)