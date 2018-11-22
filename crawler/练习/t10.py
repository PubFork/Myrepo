import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import random
import re


driver = webdriver.PhantomJS(r'C:\Users\Administrator\Desktop\Python网络班学习资料\02-Python配套PPT\26Python-爬虫\install\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.set_window_size(1080,2400)

def save_pic():
    base_dir = 'C:/Users/Administrator/Desktop/Python网络班学习资料/02-Python配套PPT/26Python-爬虫/'
    filename = '{}{:%Y%m%d%H%M%S}{}.png'.format(base_dir,datetime.datetime.now(),random.randint(1,100))
    driver.get_screenshot_as_file(filename)

driver.get('https://www.oschina.net/home/login?goto_page=https%3A%2F%2Fwww.oschina.net%2F')
save_pic()

username = driver.find_element_by_id('userMail')
username.send_keys('yuhelg@163.com')

pwd=driver.find_element_by_id('userPassword')
pwd.send_keys('yhl907625540')

pwd.send_keys(Keys.ENTER)
time.sleep(5)
save_pic()

# while True:
#     time.sleep(1)
#     try:
#         userinfo = driver.find_element_by_class_name('user_info')
#         print(userinfo.text)
#         save_pic()
#         break
#     except Exception as e:
#         print(e)

cookies = driver.get_cookies()
print(cookies)
# MAXRETRIES = 5
# for i in range(MAXRETRIES):
#     time.sleep(2)
#     try:
#         ele = driver.find_element_by_id("b_content")
#         print('ok')
#         save_pic()
#         break
#     except Exception as e:
#         print(e)

driver.close()