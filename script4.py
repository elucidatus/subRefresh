# install w/ python selenium and download chromedriver from googlesites
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib

username = ""
password = ""

driver = webdriver.Chrome('/home/elude/Downloads/chromedriver')
driver.get("https://www.aesoponline.com/login2.asp")
elem = driver.find_element_by_name("id")
elem.clear()
elem.send_keys(username)

elem2 = driver.find_element_by_name("pin")
elem2.clear()
elem2.send_keys(password)
#elem2.submit()
elem2.send_keys(Keys.RETURN)

assert "Incorrect ID or PIN combination" not in driver.page_source

# while(True): # To run forever, not in testing
job_Names = driver.find_elements_by_class_name("job")
for job in job_Names:
    if job.text:
        print job.get_attribute("id") # use this id so it only notifies once
        test = job.find_element_by_xpath(".//div[@class='locationName']") # use this to check if "HIGH SCHOOL" exist
        print test.text
        print "#" # Just a spacer
#    time.sleep(5) 
#    driver.refresh()
