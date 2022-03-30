import requests

url = 'http://apis.data.go.kr/B552061/frequentzoneOldman/getRestFrequentzoneOldman'
params ={'serviceKey' : '3dxGc3IHbMiBesCCdGuVhu%2FGdHG14z1MPsHMhc1GAGVE08pzvqwF4WbgdUobmyWGMDHvWobcgo6k2%2FMXMfh3Yw%3D%3D', 'searchYearCd' : '2015', 'siDo' : '11', 'guGun' : '320', 'type' : 'xml', 'numOfRows' : '10', 'pageNo' : '1' }

response = requests.get(url, params=params)
print(response.content)