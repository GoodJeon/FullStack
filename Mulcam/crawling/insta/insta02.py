from selenium import webdriver
from bs4 import BeautifulSoup



tag = input('search tags: ')
url = f'https://www.instagram.com/explore/tags/{tag}'

# 다운받은 webdriver를 가져와 
service = webdriver.chrome.service.Service('../drivers/chromedriver.exe')
# 경로를 설정해주고, 브라우저를 자동으로 실행시켜달라는 명령
driver = webdriver.Chrome(service=service)

# 3초 기다렸다가 url 가져와주세요.
driver.implicitly_wait(3)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_list = soup.find_all('div', class_='KL4Bh')

for img in img_list:
    print(img)
