# install w/ python selenium and download chromedriver from googlesites
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

username = ""
password = ""
fromAddr = ""
fromPass = ""
toAddr = fromAddr

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromAddr, fromPass)
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

ls_prev_id = []
while(True): # To run forever, not in testing
    job_Names = driver.find_elements_by_class_name("job")
    ls_temp_id = []
    for job in job_Names:
        job_id = job.get_attribute("id")
        ls_temp_id.append(job_id)
        if job.text and job_id not in ls_prev_id:
            test = job.find_element_by_xpath(".//div[@class='locationName']") # use this to check if "HIGH SCHOOL" exist
            date = job.find_element_by_xpath(".//td[@class='date']")
            dayL = job.find_element_by_xpath(".//span[@class='durationName']")       
            print "#" # Just a spacer
            
            msg = MIMEMultipart()
            msg['From'] = fromAddr
            msg['To'] = toAddr
            msg['Subject'] = dayL.text + " " + test.text + " " +date.text
            body = job.text
            msg.attach(MIMEText(body, 'plain'))
            server.sendmail(fromAddr,toAddr, msg.as_string())
    ls_prev_id = ls_temp_id
    time.sleep(5)
    driver.refresh()
