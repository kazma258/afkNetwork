import json
import os
import time
import platform
import subprocess
from webbrowser import Chrome
from xmlrpc.client import Server
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def myping(host):
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False


def controlnetwork():
    os.system('netsh interface set interface "Wi-Fi" admin=disabled')
    time.sleep(10)
    os.system('netsh interface set interface "Wi-Fi" admin=enabled')


def loginweb(url, name, password):
    driver = webdriver.Chrome(
        service=Server(ChromeDriverManager().install()))
    driver.get(url)
    driver.implicitly_wait(20)
    driver.find_element(By.NAME, value="username").send_keys(name)
    # 輸入密碼
    driver.find_element(By.NAME, value="password").send_keys(password)
    # 點選登入按鈕
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.quit()


def get_logininfo():
    with open(r"./LoginInfo.json") as j:
        data = json.load(j)
    return data

# 主程式
# url = r"http://www.msftconnecttest.com/redirect"
# name = "s3b017013"
# password = "efyrejkl"


info = get_logininfo()
while True:
    isOnline = myping("8.8.8.8")
    if isOnline == False:
        controlnetwork()
        loginweb(info["url"], info["username"], info["password"])
    time.sleep(int(info["sleeptime"]))
