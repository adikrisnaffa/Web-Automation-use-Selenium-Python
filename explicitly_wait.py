from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/alerts")
driver.find_element_by_xpath('//*[@id="alertButton"]').click()

try:
    WebDriverWait(driver,10).until(EC.alert_is_present())
    driver.switch_to_alert().accept()
    print("alert dipencet")

except TimeoutException :
    print("alert tidak muncul")
    pass