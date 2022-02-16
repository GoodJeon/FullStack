# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json


def getSiDo():
    url = "https://www.ministop.co.kr/MiniStopHomePage/page/store/store.do"
    resp = requests.post(url, verify=False)
    soup = BeautifulSoup(resp.text, 'html.parser')
    sido_list = soup.select('#area1 > option')
    sidos = []
    for i in range(len(sido_list)):
        if i == 0:
            continue
        else:
            sidos.append(sido_list[i].get_text())

    return sidos

def getGuGun(sido):
    url = "https://www.ministop.co.kr/MiniStopHomePage/page/store/store.do"
    resp = requests.post(url, verify=False, data={'paramInfo' : sido})
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup)


x= getSiDo()
