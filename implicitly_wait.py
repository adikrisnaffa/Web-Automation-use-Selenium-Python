from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://demoqa.com/login")
driver.get("https://demoqa.com/books")
driver.find_element_by_id("login").click()