from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

input_id = input('id 입력 : ')
input_pw = input('pw 입력 : ')


service = webdriver.chrome.service.Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# 해당 경로의 크롬 브라우저 실행
driver.get('https://www.instagram.com/accounts/login/')

# 2초간 쉬어라~
sleep(2)

# id 입력 자동화
id = driver.find_element(By.NAME, "username")
id.send_keys(input_id)

# password 입력 자동화
password = driver.find_element(By.NAME, "password")
password.send_keys(input_pw)


sleep(2)


# 로그인 버튼 클릭 자동화
driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3)").click()


# xpath는 parse tree형 절대 경로
later = driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]')
later.click()