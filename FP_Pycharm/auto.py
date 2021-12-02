from selenium import webdriver
import time
print("test case started")
#open Google Chrome browser
driver = webdriver.Chrome("D:/chromedriver_win32 (2)/chromedriver.exe")
#maximize the window size
driver.maximize_window()
#delete the cookies
driver.delete_all_cookies()
#navigate to the url
driver.get("http://127.0.0.1:5000/")
time.sleep(3)
#identify the user name text box and enter the value
driver.find_element_by_id("name").send_keys("Akshaya Venugopal")
time.sleep(3)
driver.find_element_by_id("cname").send_keys("UST Global")
time.sleep(1)
driver.find_element_by_id("number").send_keys("191788")
time.sleep(2)
driver.find_element_by_id("Email").send_keys("191788@ust-global.com")
time.sleep(2)
driver.find_element_by_id("pass").send_keys("Aks@123")
#Click on LOGIN button
driver.find_element_by_xpath("/html/body/div[2]/form/button").click()
time.sleep(5)
#close the browser
driver.close()
print("Ust login has been successfully completed")
