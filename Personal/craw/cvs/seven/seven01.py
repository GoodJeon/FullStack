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
    resp = requests.post(url, data={'Sido' : sido})
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
    resp = requests.post(url, data={'storeLaySido' : sido, 'storeLayGu': gugun, 'hiddentext':'none'})
    soup = BeautifulSoup(resp.text, 'html.parser')
    store_list = soup.select('.list_stroe > ul > li > a')
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



    return store

x = getSiDo()
y = getGuGun(x[0])
print(getStore(x[0], y[0]))

# if __name__ == '__main__':
#     print(getSiDo())
