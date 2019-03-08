import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import time


def asvabScrape():

    email = "o10428028@nwytg.net"
    driver = webdriver.Firefox()
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

    test1 = open('test1.txt', 'w', encoding="utf-8")


    while driver.find_elements_by_class_name("cBtn") != 0:

        questions = driver.find_elements_by_class_name("question")
        answers = driver.find_elements_by_class_name("answer-value")
        radios = driver.find_elements_by_class_name("answer-label")
        multiple_choice = ['A', 'B', 'C', 'D']
        radio_selector = 0

        for x in questions:
            answer_position = questions.index(x) * 4
            test1.write("\n\n %s " % (driver.find_element_by_id("sectionInfo")).text)
            test1.write("%s \n" % (x.text)) # QUESTION:
            for y in multiple_choice:
                test1.write("\t%s: %s \n" % (y, answers[answer_position].text))
                answer_position += 1
            driver.execute_script("arguments[0].click();", radios[radio_selector])
            radio_selector = radio_selector + 4


        next_button = driver.find_element_by_class_name("cBtn")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(10)




if __name__ == '__main__':
    asvabScrape()


# for x in range(45):
#     test1.write("\n\n %s " % (driver.find_element_by_id("sectionInfo")).text)
#     questions = driver.find_elements_by_class_name("question")
#     answers = driver.find_elements_by_class_name("answer-value")
#         question_selector = question_selector + 1
#         if answer_selector < len(driver.find_elements_by_class_name('answer-value')):
#             test1.write("\n")
#             test1.write("%s \n" % (driver.find_elements_by_class_name("question")[question_selector].text)) # QUESTION:
#             test1.write("\tA: %s \n" % (driver.find_elements_by_class_name('answer-value')[answer_selector].text))
#             answer_selector = answer_selector + 1
#             test1.write("\tB: %s \n" % (driver.find_elements_by_class_name('answer-value')[answer_selector].text))
#             answer_selector = answer_selector + 1
#             test1.write("\tC: %s \n" % (driver.find_elements_by_class_name('answer-value')[answer_selector].text))
#             answer_selector = answer_selector + 1
#             test1.write("\tD: %s \n" % (driver.find_elements_by_class_name('answer-value')[answer_selector].text))
#             answer_selector = answer_selector + 1
#
#
#         radio = driver.find_elements_by_class_name("answer-label")
#         driver.execute_script("arguments[0].click();", radio[radio_selector])
#         radio_selector = radio_selector + 4
#
#     question_selector = -1
#     answer_selector = 0
#     radio_selector = 0
#     print(".")
#
#     try:
#         next_button = driver.find_element_by_class_name("cBtn")
#         driver.execute_script("arguments[0].click();", next_button)
#         time.sleep(10)
#     finally:
#         pass
