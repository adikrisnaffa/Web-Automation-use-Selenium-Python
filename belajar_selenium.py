from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

#Facebook
# driver.get("https://www.facebook.com/")
# driver.find_element_by_id("email").send_keys("6285882828923")
# driver.find_element_by_name("pass").send_keys("07021996Fathya")
# driver.find_element_by_name("login").click()

#Demo Selenium
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(3)
# driver.find_element_by_css_selector("#content > div > button").click()

driver.find_element(By.XPATH,'//*[@id="content"]/div/button').click()