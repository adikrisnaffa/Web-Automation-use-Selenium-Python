from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/alerts")


driver.find_element_by_xpath('//*[@id="promtButton"]').click()
time.sleep(3)
driver.switch_to_alert().send_keys("saya sedang Test")
time.sleep(3)
driver.switch_to_alert().accept()


