# -*- coding:utf-8 -*-

import requests
import json


def getSiDo():
    # End Point : starbucks.co.kr / service url : /store/getSidoList.do
    url = "https://www.starbucks.co.kr/store/getSidoList.do"
    resp = requests.post(url)
    # resp를 json형태로 바꿔 'list'객체 가져옴
    sido_list = resp.json()['list']
    
    sido_cd = list(map(lambda x : x['sido_cd'], sido_list))
    sido_nm = list(map(lambda x : x['sido_nm'], sido_list))

    sido_dict = dict(zip(sido_cd, sido_nm))

    return sido_dict

def getGuGun(sido_cd):
    # __ajaxCall("/store/getGugunList.do", {"sido_cd":sido}, true, "json", "post", function (_response){...}
    url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    # data도 같이 보내줘야함("sido_cd")
    resp = requests.post(url, data={"sido_cd": sido_cd})
    gugun_list = resp.json()['list']

    gugun_cd = list(map(lambda x : x['gugun_cd'], gugun_list))
    gugun_nm = list(map(lambda x : x['gugun_nm'], gugun_list))

    gugun_dict = dict(zip(gugun_cd, gugun_nm))

    return gugun_dict

def getStore(sido_cd='', gugun_cd=''):
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    resp = requests.post(url, data={'ins_lat': '37.3653504',
                                    'ins_lng': '126.9399552',
                                    'p_sido_cd': sido_cd,
                                    'p_gugun_cd': gugun_cd,
                                    'in_biz_cd': '',
                                    'set_date': ''})
    store_list = resp.json()['list']
    # s_name, tel, doro_address, lat, lot
    result_list = list()
    for store in store_list:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        result_list.append(store_dict)
    # print(result_list)

    # {'store_list': [{},{},{}]}
    result_dict = dict()
    result_dict['store_list'] = result_list
    # print(result_dict)



    # json으로 저장
    result_json = json.dumps(result_dict, ensure_ascii=False)

    with open('starbucks01.json', 'w', encoding='utf-8') as f:
        f.write(result_json)

    return result_json





if __name__ == '__main__':
    print(getSiDo())
    sido = input('도시 코드를 입력해 주세요 : ')
    if sido == '17':
        print(getStore(sido_cd='17', gugun_cd=''))
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해 주세요 : ')
        print(getStore(gugun_cd=gugun))