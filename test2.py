import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys as keys
import os
from time import sleep 
import re
from configdata import id,pw,chromedriver_dir,user

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
for i in driver.find_elements_by_class_name("article"):
    if i.get_attribute("href") != None:
        flag = True
        text = i.get_attribute("textContent")
        for u in user:
            if not u in text:
                flag = False
        if flag:
            url_list.append(i.get_attribute("href"))
            
for i in url_list:
    print(i)
    driver.get(i)
    sleep(1)
    for j in driver.find_elements_by_class_name("article"):
        if j.get_attribute("href") != None:
            url_list2.append(j.get_attribute("href"))

from urllib.parse import urlparse,parse_qs
import mjParse
kyoku_list = []
for i in url_list2:
    flag = True
    while flag:
        try:
            driver.get(i)
            sleep(2)
            title = re.sub(r"  |\n|\t", " ", driver.find_element_by_class_name("head_article").get_attribute("textContent")).replace(u"\xa0",u" ").split()
            saiseki = re.sub(r"  |\n|\t", " ", driver.find_element_by_class_name("body").get_attribute("textContent")).replace(u"\xa0",u" ").split()
            url = driver.find_element_by_id("browser_play").get_attribute("href")
            url_parse = urlparse(url)
            o = parse_qs(url_parse.query)
            OYA = int(o["B"][0][3])
            tmp = [title,saiseki]
            tmp.append(mjParse.N(o["N"][0],OYA))
            tmp.append(mjParse.get_test(mjParse.A(o["A"][0],OYA)))
            kyoku_list.append(tmp)
            flag = False
            print(tmp)
        except Exception as e:
            print(e.args)
            sleep(30)
