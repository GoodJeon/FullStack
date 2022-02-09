# -*- coding:utf-8 =*-
from bs4 import BeautifulSoup
import requests
import json

url = 'https://comic.naver.com/webtoon/weekdayList?week=wed'
resp = requests.get(url)
# print(resp)
# print(resp.text)

soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

webtoons = soup.find('ul', class_='img_list')


dl_list = webtoons.select('dl')


lst = list()
for dl in dl_list:
    title = dl.find('a')['title']
    star = dl.find('strong').text

    tmp = dict()
    tmp['title'] = title
    tmp['star'] = star
    lst.append(tmp)

# print(lst)
res = dict()
res['webtoons'] = lst
# print(res)
res_json = json.dumps(res, ensure_ascii=False) # 아스키코드로 인코딩 되는 것을 방지
print(res_json)

with open('webtoons.json', 'w', encoding='utf-8') as f:
    f.write(res_json)