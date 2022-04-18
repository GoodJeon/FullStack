# -*- coding:utf-8 -*-
import requests
from xml.etree import ElementTree
from collections import Counter

url = 'http://apis.data.go.kr/B552895/LocalGovPriceInfoService/getItemPriceResearchSearch'
arr = []
for i in range(1, 5):
    for j in range(1, 32):
        if len(str(j)) == 1:
            params ={'serviceKey' : 'G8/6kLlqz2GninZfrl6HupkMdDQuH84vtXL9uJ7Pp8fYP7EhO8JJADYKZCJlTCZd0AbiIy9pCJP+151EAPYwRw==', 'numOfRows' : '4000', '_returnType' : 'xml', 'examin_de' : f'20220{str(i)}0{str(j)}'}    
        else:
            params ={'serviceKey' : 'G8/6kLlqz2GninZfrl6HupkMdDQuH84vtXL9uJ7Pp8fYP7EhO8JJADYKZCJlTCZd0AbiIy9pCJP+151EAPYwRw==', 'numOfRows' : '4000', '_returnType' : 'xml', 'examin_de' : f'20220{str(i)}{str(j)}'}

        response = requests.get(url, params=params)
        tree = ElementTree.fromstring(response.text)
        # print(len(tree[-1][0]))

        for item in tree[-1][0] :
            arr.append(item.find('prdlst_nm').text)


pum_name = list(Counter(arr).keys())
pum_count = list(Counter(arr).values())
print(pum_name, pum_count)
