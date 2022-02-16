# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}


url = "https://www.melon.com/chart/index.htm"

resp = requests.get(url, headers = headers)
soup = BeautifulSoup(resp.text, 'html.parser')

# TOP100 차트 제목 가져오기
title_divs = soup.find_all('div',{'class':'ellipsis rank01'})
titles = []
for div in title_divs:
    title = div.find('a').get_text()
    titles.append(title)

print(titles)

# 가수명 가져오기
singer_divs = soup.find_all('div',{'class':'ellipsis rank02'})
singers = []
for div in singer_divs:
    singer = div.find('a').get_text()
    singers.append(singer)
print(singers)



chart_list = list(zip(titles, singers))
chart = []
for data in chart_list:
    song = {}

    song['title'] = data[0]
    song['singer'] = data[1]
    chart.append(song)
print(chart)

