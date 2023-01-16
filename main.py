from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pathlib
from pathlib import Path
from time import sleep
import datetime


def main():
    browser = webdriver.Firefox()
    browser.get('https://vk.com/login')
    current = browser.current_url
    if current == 'https://vk.com/login':
        vk_login(browser)
    sleep(1)
    send_message(browser)

def vk_login(browser):
    name = 'vk_login.txt'
    path = Path(pathlib.Path().absolute(), name)
    with open(path, 'r') as file:
        lines = file.readlines()
        login = lines[0][6:].strip()
        password = lines[1][9:].strip()
    s_username = browser.find_element(By.ID, 'index_email')
    s_continue = browser.find_element(By.CLASS_NAME, 'FlatButton__content')
    s_username.send_keys(login)
    s_continue.click()
    sleep(1)
    s_password = browser.find_element(By.NAME, 'password')
    s_password.send_keys(password)
    s_continue = browser.find_element(By.CLASS_NAME, 'vkuiButton__in')
    s_continue.click()


def send_message(browser):
    name = 'configuration.txt'
    path = Path(pathlib.Path().absolute(), name)
    with open(path, 'r') as file:
        lines = file.readlines()
        url = lines[0][4:].strip()
        message = lines[1][8:].strip()
        time = lines[2][5:].strip()
        print(url, message, time)
    browser.get(url)
    sleep(1)
    s_message = browser.find_elements(By.CLASS_NAME, "im-chat-input--text")[0]
    flag = True
    while flag:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == time:
            sleep(1)
            s_message.send_keys(message)
            s_message.send_keys(Keys.RETURN)
            flag = False


if __name__ == "__main__":
    main()