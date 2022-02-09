from bs4 import BeautifulSoup
import requests


url='https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=5'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
titles = soup.find_all('span', class_='title')

for title in titles:
    print(title.text.strip())


lst = list()
pages = soup.select('.pagination a')

for page in pages:
    if len(page.text) <= 2:
        lst.append(page.text)

for i in lst:
    url = f'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage={i}'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    titles = soup.find_all('span', class_='title')
    for title in titles:
        print(title.text.strip())
