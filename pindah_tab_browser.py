from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

#Pindah tab Browser
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_link_text("Click Here").click()
time.sleep(4)
driver.switch_to_window(driver.window_handles[0])