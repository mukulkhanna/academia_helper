
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser=webdriver.Chrome('../../../Documents/chromedriver')
browser.get('http://academia.srmuniv.ac.in')
frame = browser.find_element_by_xpath("//iframe[@urltype='zc_cpLoginUrl']")
browser.switch_to_frame(frame)
WebDriverWait(browser, 3).until(
    EC.frame_to_be_available_and_switch_to_it((By.NAME, "zohoiam"))
    )
browser.find_element_by_xpath("//input[@id='Email']").send_keys("mukulkhanna_ra@srmuniv.edu.in")
browser.find_element_by_xpath("//input[@id='Password']").send_keys("dafuqsrm")
browser.find_element_by_xpath("""//*[@id="signinForm"]/div[5]/input""").click()

#logged in till this point ^
#browser.implicitly_wait(15)

WebDriverWait(browser,25).until(
    EC.presence_of_element_located((By.XPATH,"""//*[@id="zc-container"]/tbody/tr[1]/td/div[5]/table/tbody/tr/td[6]""")))
browser.find_element_by_xpath("""//*[@id="zc-container"]/tbody/tr[1]/td/div[5]/table/tbody/tr/td[6]""").click()


