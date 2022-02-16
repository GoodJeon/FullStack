# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json

store_list = []

for i in range(2001, 3001):
    url = f'http://cu.bgfretail.com/store/list_Ajax.do?pageIndex={i}&listType=&jumpoCode=&jumpoLotto=&jumpoToto=&jumpoCash=&jumpoHour=&jumpoCafe=&jumpoDelivery=&jumpoBakery=&jumpoFry=&jumpoAdderss=&jumpoSido=&jumpoGugun=&jumpodong=&user_id=&sido=&Gugun=&jumpoName='

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    names = soup.findAll('span', {'class':'name'})
    tels = soup.findAll('span', {'class':'tel'})
    addresses = soup.select('address > a')

    for i in range(5):
        store = {}
        store['s_name'] = names[i].get_text()
        store['tel'] = tels[i].get_text()
        store['doro_address'] = addresses[i].get_text()
        store_list.append(store)

result_dict = {}
result_dict['store_list'] = store_list

result_json = json.dumps(result_dict, ensure_ascii=False)

with open('../data/cu03.json', 'w', encoding='utf-8') as f:
    f.write(result_json)


