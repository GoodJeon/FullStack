from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException, ElementNotInteractableException,NoSuchWindowException, NoSuchFrameException
from bs4 import BeautifulSoup
import requests
from time import sleep
import pandas as pd
import json
from collections import OrderedDict


# 서울시 음식점 데이터 불러오기
df_seoul = pd.read_csv('seoul_total.csv')
## 식당 명
name = df_seoul['s_name']
## XX구 -> XX으로 바꾸는 작업. ex) 용산구 -> 용산
gu = df_seoul['s_add'].str.split(' ', expand=True)[1].str[:-1]
## 도로명 주소(대로)
road = df_seoul['s_road'].str.split(' ', expand=True)[2]


# 망고플레이트 검색 페이지로 시작
url = f'https://www.mangoplate.com/search/시작'

# 다운 받은 webdriver를 가져와
service = webdriver.chrome.service.Service('chromedriver.exe')
# 경로를 설정해주고, 브라우저를 자동으로 실행하는 명령을 driver에 저장해준다.
driver = webdriver.Chrome(service=service)
# 기다렸다가 url 가져오기
driver.implicitly_wait(1) 
driver.get(url)



# 팝업창 끄기
## 프레임으로 이동 
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
## 닫기 버튼 누르고
driver.find_element(By.CSS_SELECTOR, '.ad_btn_wrap:nth-child(2)').click()
## 기존 HTML문서로 다시 복귀
driver.switch_to.default_content()




# 개수 세기위한 count 정의
count = 0
seoul = []






# 서울시 음식점 데이터 가져와서 그 크기만큼 반복문 실행

for i in range(len(df_seoul)):
    # 검색창에 값 입력 후 Enter키
    driver.find_element(By.XPATH, '/html/body/header/div/label/input').send_keys(gu[i] + ' ' + name[i])
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/header/div/label/input').send_keys(Keys.ENTER)
    sleep(2)


    
    # dict 형태 만들기
    store = {}
    


    # 식당이 존재한다면 클릭 시도
    try:
        store['id'] = count
        # 검색 후 처음 나오는 식당을 선택
        first = driver.find_element(By.XPATH, '/html/body/main/article/div[2]/div/div/section/div[3]/ul/li[1]/div[1]')
        first.click()
        sleep(1)
        
        print(road[i])
        print(driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[1]/td').text.split(' ')[2])
        # 해당 주소가 맞는지 도로명주소의 3번째 요소를 가지고 비교
        if road[i] == driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[1]/td').text.split(' ')[2]:
            
            # 상점명
            # 만약 지점 데이터가 있다면 상점명 + 지점명
            if driver.find_element(By.CSS_SELECTOR, '.branch') == NoSuchElementException:
                store['s_name'] = driver.find_element(By.CSS_SELECTOR, '.restaurant_name').text
            else:
                store['s_name'] = (driver.find_element(By.CSS_SELECTOR, '.restaurant_name').text + ' ' + driver.find_element(By.CSS_SELECTOR, '.branch').text).strip()
                

            # 주소명
            ## 지번이 있으면 지번도 가져오기!
            if driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[1]/td/span[2]') == NoSuchElementException:
                store['s_road'] = driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[1]/td').text.split('\n')[0]
            else:
                store['s_road'] = driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[1]/td').text.split('\n')[0]
                store['s_add'] = driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[1]/td/span[2]').text
                

            # 전화번호
            if driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[2]/td') == NoSuchElementException:
                pass
            else:
                store['s_tel'] = driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[2]/td').text

            # 음식 종류
            if driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[3]/td') == NoSuchElementException:
                pass
            else:
                store['s_repre'] = driver.find_element(By.XPATH, '/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[3]/td').text 

            
            # 만약 가격대 이후로 테이블에 상세정보가 존재할 경우에 대해서 코딩
            ## 상세정보는 주소, 전화번호, 음식 종류, 가격대는 고정으로 나와있다.
            ## 그 외의 것들에는 ' 메뉴, 주차, 영업시간, 쉬는시간, 마지막 주문, 휴일, 웹 사이트 ' 가 있다.
            
            # 상세정보 테이블을 가져와서
            table = driver.find_element(By.CSS_SELECTOR, 'body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody')
            # tr의 개수를 세준다.
            tr = table.find_elements_by_tag_name('tr')
            print(len(tr))
            # 그리고 5번째부터 tr의 총 개수까지 반복
            for i in range(5, len(tr)+1):
                what = driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]')
                if what == NoSuchElementException:
                    pass
                else:
                    # 메뉴(문자 형태만)
                    if driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/th').text == '메뉴' and driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/td').text != '' : 
                        store['s_menu'] = []
                        menus = driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/td').text
                        split_menus = menus.split('\n')
                        for i in range(0, len(split_menus), 2):
                            menu = {}
                            f_name = split_menus[i]
                            f_price = split_menus[i+1]
                            menu[f_name] = f_price
                            store['s_menu'].append(menu)

                    # 주차
                    elif driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/th').text == '주차':
                        store['s_parking'] = driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/td').text
                    # 영업시간
                    elif driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/th').text == '영업시간':
                        store['s_hour'] = driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/td').text
                    # 쉬는시간
                    elif driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/th').text == '쉬는시간':
                        store['s_break'] = driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/td').text
                    # 마지막주문
                    elif driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/th').text == '마지막주문':
                        store['s_lastorder'] = driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/td').text
                    # 휴일
                    elif driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/th').text == '휴일':
                        store['s_holiday'] = driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/td').text
                    # 웹 사이트
                    elif driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/th').text == '웹 사이트':
                        store['s_link'] = driver.find_element(By.XPATH, f'/html/body/main/article/div[1]/div[1]/div/section[1]/table/tbody/tr[{i}]/td/a').get_attribute('href')


            seoul.append(store)
            count += 1


        else:
            seoul.append(store)
            count += 1
            pass
            

        



        


    except NoSuchElementException:
        count += 1
        seoul.append(store)
        pass
    
    # 100개의 상점마다 파일 덮어쓰기
    if count % 1 == 0:
        mango = OrderedDict()
        mango['store'] = seoul
        with open('mango.json', 'w', encoding='utf-8') as f:
            json.dump(mango, f, ensure_ascii=False, indent = "\t")

    
    






