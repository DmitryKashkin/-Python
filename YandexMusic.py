from selenium import webdriver
import selenium
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.key_actions import KeyActions
import pickle


def yandex():
    EXE_PATH = r'chromedriver.exe'
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    driver.get(
        'https://yandex.ru')
    sleep(1)
    element = driver.find_element('id', 'text')
    element.send_keys('dsfdsfsdf')
    sleep(1)
    action.send_keys(Keys.RETURN)
    action.perform()
    sleep(100)


def yandex_music():
    EXE_PATH = r'chromedriver.exe'
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    driver.get(
        'https://passport.yandex.ru/auth?origin=music_button-header&retpath=https%3A%2F%2Fmusic.yandex.ru%2Fsettings%3Freqid%3D42336580116627399272688109178242113%26from-passport')
    sleep(1)
    element = driver.find_element(By.CLASS_NAME, 'AuthLoginInputToggle-type')
    element.click()
    element_login = driver.find_element('id', 'passp-field-login')
    element_login.send_keys('m7842066' + Keys.RETURN)
    sleep(2)
    element_pass = driver.find_element('id', 'passp-field-passwd')
    element_pass.send_keys('Pim$h@srh@12' + Keys.RETURN)
    sleep(1)
    action.send_keys(Keys.RETURN)
    action.perform()
    input('continue?')

    try:
        element=driver.find_element(By.CLASS_NAME, 'pay-promo-close-btn js-close')
    except selenium.common.exceptions.NoSuchElementException:
        pass
    else:
        element.click()
    driver.get('https://music.yandex.ru/home')
    sleep(3)
    element = driver.find_element(By.CLASS_NAME, 'rup__content-button')
    element.click()
    input('continue?')
    element = driver.find_element(By.CLASS_NAME, 'K390 I4mG') # Play
    element.click()
    # element=driver.find_element(By.CLASS_NAME,'K390 I4mG')

    while True:
        pass


if __name__ == '__main__':
    yandex_music()
