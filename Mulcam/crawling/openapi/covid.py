from xml.etree import ElementTree
import requests
import re

service_key='VXBYQ69L5Fwe5N6ROU%2BQDFRw2QT7VAQq2iW9WUSFjTxT5tCatN27CjwGwFKDLtqMhSaBV2BfjIAhytbw2lcWmg%3D%3D'

url = f'http://apis.data.go.kr/B552061/frequentzoneFreezing?ServiceKey={service_key}'


resp = requests.get(url)
# print(resp.text)
tree = ElementTree.fromstring(resp.text)

for item in tree[1][0]:
    # print(item.find('gubun').text)
    if item.find('gubun').text == '합계':
        stdDay = re.sub(r'(\D)+', '', item.find('stdDay').text)
        stdDay = stdDay[2:4] + "/" + stdDay[4:6] + "/" + stdDay[6:8]
        incDec = item.find('incDec').text
        localOccCnt = item.find('localOccCnt').text
        overflowCnt = item.find('overFlowCnt').text
        print(f'[{stdDay}]')
        print(f"일일합계:{incDec}")
        print(f"국내발생:{localOccCnt}")
        print(f"해외발생:{overflowCnt}")

