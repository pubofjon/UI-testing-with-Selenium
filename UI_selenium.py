# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import datetime as datetime
import time
from datetime import timedelta

def UI_test_with_Se(ticker=''):

    from lxml import html
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import TimeoutException

    chrome_options=Options()
    chrome_options.add_argument("--disable-popup")
    chrome_options.add_extension(r"c:\pycode\Github\extension_1_0_7_overlay_remove.crx")
    chrome_options.add_extension(r"c:\pycode\Github\extension_1_13_8.crx")  #fairad
    #chrome_options.add_extension(r"G:\Trading\Trade_python\pycode\Github\extension_0_3_4.crx")
    chrome_options.add_argument('--always-authorize-plugins=true')
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")  #full screen
    x=r"C:\Users\jon\AppData\Local\Google\Chrome\User Data\Default"
    chrome_options.add_argument("user-data-dir=%s"%x)
    
    url ="https://where_to_test/"
    gecko="c:\\pycode\Github\chromedriver.exe"
    driver=webdriver.Chrome(executable_path="c:\pycode\Github\chromedriver.exe", \
        chrome_options=chrome_options)
    
    driver.get(url)

    try:
        ol=driver.find_element_by_class_name("register-flyer-close")
        ol=driver.find_element
        ol.click()
    except:
        print("no find flyer close")
        pass
    username = driver.find_element_by_id("UserName")
    password = driver.find_element_by_id("Password")
    username.send_keys("id")
    password.send_keys("pswd")
    submit=driver.find_element_by_xpath('//input[@class="site-login-control btn"]')
   
    
    item_to_test=driver.find_element_by_xpath('//*[@id="symov_main_sidebar"]/div[1]/div[3]/div[6]/span[2]').get_attribute('textContent')


    driver.close()
    driver.quit()
    return

