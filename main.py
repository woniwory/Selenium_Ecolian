from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
# 크롬 드라이버
driver = webdriver.Chrome('C:\\Users\\woniw\\OneDrive\\바탕 화면\\chromedriver_win32\\chromedriver.exe')

# URL
url = 'https://m.ecolian.or.kr:444/asp/rsvn/login.asp?returnUrl=https%3A%2F%2Fm.ecolian.or.kr%3A444%2Fasp%2Frsvn%2FrsvnStep1.asp'
driver.get(url)
driver.maximize_window()

driver.find_element_by_id('f_id').send_keys('kysuzgolf')
driver.find_element_by_id('f_pw').send_keys('(K$344247')
pyautogui.press('Enter')
time.sleep(0.3)


# driver.find_element_by_id('f_bsns').click()
# driver.find_element_by_xpath('*//button[text()="에콜리안 제천"]')
# driver.find_element("33").click()
# driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('')





def Refresh():
    time.sleep(0.2)
    driver.find_element_by_id('btnCalNext').click()
    time.sleep(0.2)
    SENTINEL = check()

    if SENTINEL == 1:
        return

    time.sleep(0.1)
    driver.find_element_by_id('btnCalPrev').click()
    time.sleep(0.15)
    SENTINEL = check()

    if SENTINEL == 1:
        return

    Refresh()



def check():
    rgb = getPixel(btn)
    print(rgb)
    if rgb == ((106, 163, 73) or (107, 164, 74) or (37, 104, 0)):
        print("check()함수 ")
        SENTINEL = Macro()
        return SENTINEL


def Macro():
    pyautogui.click(btn)  # 6일 선택 ####
    pyautogui.press('Enter')

    SENTINEL = hourchoice()
    if SENTINEL == 0:
        safelist(len(hourlist) - 1, hourlist, 800)

    SENTINEL = minutechoice()
    if SENTINEL == 0:
        safelist(len(minutelist) - 1, minutelist, 840)

    pyautogui.click(192, 904)  # 다음 단계

    time.sleep(0.6)
    pyautogui.click(192, 564)
    pyautogui.click(192, 628)  # 4명 (제천, 영광, 거창)

    pyautogui.click(192, 653)  # 2번째 동반자
    pyautogui.write("wjdakstjq")

    time.sleep(0.2)
    pyautogui.click(518, 700)  # 3번째 동반자
    pyautogui.write("wjdrudtjq")

    pyautogui.click(518, 725)  # 4번째 동반자
    pyautogui.write("answjdtnr")

    pyautogui.click(1915, 970)  # 예약신청

    return 1
#     # URL
#     url = 'https://google.com'
#     driver.get(url)
#
#     # 요소
#     #elem = driver.find_element_by_class_name('link_login')
#
#     # 요소 클릭
#     #elem.click()
#
#     driver.switch_to_alert()
# except Exception as e:
#     print(e)
#
# finally:
#     # 드라이버 종료
#     driver.close()
#     print('닫기')
