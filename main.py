import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import time
import requests as rq
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('C:\\Users\\woniw\\OneDrive\\바탕 화면\\chromedriver_win32 (1)\\chromedriver.exe')
# URL
url = 'https://m.ecolian.or.kr:444/asp/rsvn/login.asp?returnUrl=https%3A%2F%2Fm.ecolian.or.kr%3A444%2Fasp%2Frsvn%2FrsvnStep1.asp'
id = 'kysuzgolf'
pw = '(K$344247'

driver.get(url)
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "f_id")))
driver.find_element_by_id('f_id').send_keys(id)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "f_pw")))
driver.find_element_by_id('f_pw').send_keys(pw)
time.sleep(1)
pyautogui.press('Enter')
time.sleep(1)

#id jms0805
#pw Ch08jms8828*

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#f_bsns > option:nth-child''(3)')))
driver.find_element_by_css_selector('#f_bsns > option:nth-child'
                                    '(4)').click()  # 4제천
time.sleep(0.3)
driver.find_element_by_css_selector('#btnCalNext') .click()#예약할 달로 세팅

xpath = input("예약할 버튼의 xpath를 입력해주세요")
def Macro():
    print('Execute Macro Program.')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "f_hour"] / option[2]')))
    driver.find_element_by_xpath('// *[ @ id = "f_hour"] / option[4]').click() # // *[ @ id = "f_hour"] / option[1] 은 '시간 선택'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="f_minute"]/option[2]')))
    driver.find_element_by_xpath('//*[@id="f_minute"]/option[4]').click() # // *[ @ id = "f_minute"] / option[1] 은 '분 선택'

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnStep2"]')))
    driver.find_element_by_xpath('//*[@id="btnStep2"]').click()

    time.sleep(0.1)
    pyautogui.press('Enter')



    time.sleep(0.6)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'f_player_cnt')))
    driver.find_element_by_id('f_player_cnt')
    driver.find_element_by_css_selector('#f_player_cnt > option:nth-child(2)').click()
    driver.find_element_by_css_selector('#f_player_name0').send_keys('###')
    driver.find_element_by_css_selector('#f_player_name1').send_keys('###')
    driver.find_element_by_css_selector('#f_player_name2').send_keys('###')
    driver.find_element_by_css_selector('#f_player_name3').send_keys('###')

    driver.find_element_by_css_selector('#btnSubmit').click() #예약신청

    return 1


def check(xpath):
    available = "ResvDate item rsvn"
    tmp_xpath = xpath
    if driver.find_element_by_xpath(tmp_xpath).get_attribute('class') == available:
        driver.find_element_by_xpath(tmp_xpath).click()
        alert = driver.switch_to.alert
        alert.accept()
        print('Detected')
        SENTINEL = Macro()
        return SENTINEL



while True:

    print()
    print("    1. Program 실행")
    print("    2. Settings ")  # 확장성 : 이벤트 발생시 처리 구현
    print("    3. 종료")
    print()
    print("=" * 34)
    print()
    choice = int(input("원하시는 기능을 선택해주세요 : "))

    if choice == 1:
        SENTINEL = 0
        while (SENTINEL != 1):
            time.sleep(0.2)
            driver.find_element_by_id('btnCalPrev').click()
            time.sleep(0.2)
            SENTINEL = check(xpath)

            time.sleep(0.2)
            driver.find_element_by_id('btnCalNext').click()
            time.sleep(0.2)
            SENTINEL = check(xpath)

    elif choice == 2:

        print("현재 ID :",id)
        print("현재 PW :",pw)

        id = input("변경할 ID를 입력하세요 : ")
        pw = input("변경할 PW를 입력하세요 : ")


    elif choice == 3:  # 프로그램 종료
        print("프로그램을 종료합니다.")
        print()
        print("=" * 34)
        break

    else:
        print("잘못된 입력입니다.")
        continue











