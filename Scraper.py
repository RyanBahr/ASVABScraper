import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import time



test1 = open('test1.txt', 'w', encoding="utf-8")

email = "o10428028@nwytg.net"

driver = webdriver.Firefox()
driver.implicitly_wait(45) # seconds

driver.get("https://secure.military.com/Recruiting/first?lpid=asvab&asvab=yes")

driver.find_element_by_id("inputEmail").send_keys(email)

driver.find_element_by_id("selectMonth").click()

driver.find_element_by_xpath('//*[@id="selectMonth"]/option[2]').click()

driver.find_element_by_id("selectDay").click()

driver.find_element_by_xpath('//*[@id="selectDay"]/option[2]').click()

driver.find_element_by_id("selectYear").click()

driver.find_element_by_xpath('//*[@id="selectYear"]/option[22]').click()

zip = driver.find_element_by_id("inputZip")
zip.send_keys(12345)

driver.find_element_by_id("submit").click()

driver.find_element_by_xpath('//*[@id="entryform"]/div[1]/div[13]/span[2]/a').click()

# driver.get("https://www.military.com/asvab-test/practice/4")
driver.get("https://www.military.com/asvab-test/practice/5")
# driver.get("https://www.military.com/asvab-test/practice/6")

question_selector = -1
answer_selector = 0
radio_selector = 0

for x in range(45):
    test1.write("\n\n %s " % (driver.find_element_by_id("sectionInfo")).text)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cBtn")))
    finally:
        pass
    driver.implicitly_wait(60)
    for x in driver.find_elements_by_class_name("question"):
        question_selector = question_selector + 1
        if answer_selector < len(driver.find_elements_by_class_name('answer-value')):
            test1.write("\n")
            test1.write("%s \n" % (driver.find_elements_by_class_name("question")[question_selector].text)) # QUESTION:
            test1.write("\tA: %s \n" % (driver.find_elements_by_class_name('answer-value')[answer_selector].text))
            answer_selector = answer_selector + 1
            test1.write("\tB: %s \n" % (driver.find_elements_by_class_name('answer-value')[answer_selector].text))
            answer_selector = answer_selector + 1
            test1.write("\tC: %s \n" % (driver.find_elements_by_class_name('answer-value')[answer_selector].text))
            answer_selector = answer_selector + 1
            test1.write("\tD: %s \n" % (driver.find_elements_by_class_name('answer-value')[answer_selector].text))
            answer_selector = answer_selector + 1


        radio = driver.find_elements_by_class_name("answer-label")
        driver.execute_script("arguments[0].click();", radio[radio_selector])
        radio_selector = radio_selector + 4

    question_selector = -1
    answer_selector = 0
    radio_selector = 0
    print(".")

    try:
        next_button = driver.find_element_by_class_name("cBtn")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(10)
    finally:
        pass
