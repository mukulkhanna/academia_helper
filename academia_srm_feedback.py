
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random

browser=webdriver.Chrome('../../../Documents/chromedriver')
browser.get('http://academia.srmuniv.ac.in')
frame = browser.find_element_by_xpath("""//*[@id="signinPage"]/div[2]/iframe""")
browser.switch_to_frame(frame)
WebDriverWait(browser,25).until(
    EC.presence_of_element_located((By.XPATH,"""//input[@id='Email']""")))
browser.find_element_by_xpath("//input[@id='Email']").send_keys("")
browser.find_element_by_xpath("//input[@id='Password']").send_keys("")
browser.find_element_by_xpath("""//*[@id="signinForm"]/div[5]/input""").click()

#logged in till this point ^

WebDriverWait(browser,25).until(
    EC.presence_of_element_located((By.XPATH,"""//*[@id="zc-container"]/tbody/tr[1]/td/div[5]/table/tbody/tr/td[7]""")))  #waiting for row-element to load

#waiting for table rows to load ^

select_span=browser.find_element_by_xpath("""//*[@id="zc-container"]/tbody/tr[1]/td/div[5]/table/tbody/tr/td[7]""")

select_span.click()
time.sleep(10)       
actions = ActionChains(browser) 
actions.send_keys(Keys.TAB * 6)
for j in range(0,7):
    for i in range(0,14):
        actions.send_keys(Keys.DOWN * random.randint(1, 5))
        actions.send_keys(Keys.ENTER * 1)
    actions.send_keys(Keys.TAB * 3)
               
actions.send_keys(Keys.TAB * 2)

for j in range(0,4):
    for i in range(0,14):
        actions.send_keys(Keys.DOWN * random.randint(1, 5))
        actions.send_keys(Keys.ENTER * 1)
    
    actions.send_keys(Keys.TAB * 3)
    
actions.perform()

time.sleep(2)
browser.find_element_by_xpath("""//*[@id="Student_Feedback_Form_2016_17_3"]/div[1]/form/table/tbody/tr/td/span/input[1]""").click()
