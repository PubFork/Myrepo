import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import datetime
import random
import re


driver = webdriver.PhantomJS(r'C:\Users\Administrator\Desktop\Python网络班学习资料\02-Python配套PPT\26Python-爬虫\install\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.set_window_size(1080,2400)

def save_pic():
    base_dir = 'C:/Users/Administrator/Desktop/Python网络班学习资料/02-Python配套PPT/26Python-爬虫/'
    filename = '{}{:%Y%m%d%H%M%S}{}.png'.format(base_dir,datetime.datetime.now(),random.randint(1,100))
    driver.get_screenshot_as_file(filename)

driver.get('https://movie.douban.com/')

try:
    ele = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,'//input[@id="inp-query"]')))
    ele.send_keys("TRON")
    ele.send_keys(Keys.ENTER)
except Exception as e:
    print(e)


