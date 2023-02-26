from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import json

f = open('data.json', 'w', encoding='utf-8')
browser = webdriver.Chrome()
action = ActionChains(browser)
browser.get('https://www.xilazimu.net/m/articles/greek_letter_latex.html')
result = {'result': []}
ele = browser.find_elements(By.XPATH, '/html/body/div[2]/div/div/div/div/table[1]/tbody/tr/td[2]')
for i in ele:
    result['result'].append(i.text[1:])
json.dump(result, f)