from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/droppable")
driver.maximize_window()
driver.implicitly_wait(10)

elemen = driver.find_element_by_id("draggable")
kotak = driver.find_element_by_id("droppable")

action = ActionChains(driver)

action.drag_and_drop(elemen, kotak).perform()