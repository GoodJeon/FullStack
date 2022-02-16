# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json


def getSiDo():
    url = "https://www.7-eleven.co.kr/util/storeLayerPop.asp"
    resp = requests.post(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    sido_list = soup.select('#storeLaySido > option')
    sidos = []
    for i in range(len(sido_list)):
        if i == 0:
            continue
        else:
            sidos.append(sido_list[i].get_text())

    return sidos


def getGuGun(sido):
    url = 'https://www.7-eleven.co.kr/library/asp/StoreGetGugun.asp'
    resp = requests.post(url, data={'Sido': sido})
    soup = BeautifulSoup(resp.text, 'html.parser')
    gugun_list = soup.select('option')
    guguns = []
    for i in range(len(gugun_list)):
        if i == 0:
            continue
        else:
            guguns.append(gugun_list[i].get_text())
    return guguns


def getStore(sido, gugun):
    url = 'https://www.7-eleven.co.kr/util/storeLayerPop.asp'
    resp = requests.post(url, data={'storeLaySido': sido, 'storeLayGu': gugun, 'hiddentext': 'none'})
    soup = BeautifulSoup(resp.text, 'html.parser')
    store_list = soup.select('.list_stroe > ul > li > a')
    result_list = []
    for i in store_list:
        store = {}
        # 매장명
        store['s_name'] = i.find('span').get_text().strip()

        # 도로명 주소
        store['doro_address'] = i.find_all('span')[1].get_text()

        # 위도(lat), 경도(lot) 가져오기
        a = i['href'].split(',')
        a.pop(0)
        a[1] = a[1][:-2]
        store['lat'] = a[0]
        store['lot'] = a[1]
        result_list.append(store)

    return result_list




if __name__ == '__main__':
    list_all = []
    sido_all = getSiDo()
    for sido in sido_all:
        gugun_all = getGuGun(sido)
        for gugun in gugun_all:
            result = getStore(sido, gugun)
            # print(result)

            list_all.extend(result)


result_dict = {}
result_dict['store_list'] = list_all

result = json.dumps(result_dict, ensure_ascii=False)

with open('../data/seveneleven_all.json', 'w', encoding='utf-8') as f:
    f.write(result)
