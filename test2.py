import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys as keys
import os
from time import sleep 
import re
from configdata import id,pw,chromedriver_dir

global options
options = Options()
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')

driver = webdriver.Chrome(chromedriver_dir, chrome_options=options)

driver.get("https://pl.sega-mj.com/players/login")
driver.find_element_by_name("mjm_id").send_keys(id)
driver.find_element_by_name("password").send_keys(pw)
driver.find_element_by_id("login").click()
sleep(1)
driver.get("https://pl.sega-mj.com/playdata_view/showHistory")
sleep(1)
url_list = []
url_list2 = []
# print(driver.find_elements_by_xpath('//a[class="article normal"]'))
for i in driver.find_elements_by_class_name("article")[:2]:
    if i.get_attribute("href") != None:
        url_list.append(i.get_attribute("href"))
for i in url_list:
    print(i)
    driver.get(i)
    sleep(1)
    for j in driver.find_elements_by_class_name("article")[:2]:
        if j.get_attribute("href") != None:
            url_list2.append(j.get_attribute("href"))

from urllib.parse import urlparse,parse_qs
import mjParse
for i in url_list2:
    driver.get(i)
    sleep(1)
    url = driver.find_element_by_id("browser_play").get_attribute("href")
    url_parse = urlparse(url)
    o = parse_qs(url_parse.query)
    OYA = int(o["B"][0][3])
    print("名前:",mjParse.N(o["N"][0],OYA))
    print(mjParse.get_test(mjParse.A(o["A"][0],OYA)))
input()
