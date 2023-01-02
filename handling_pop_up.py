from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

driver.get("https://getbootstrap.com/docs/4.0/components/modal/")
driver.find_element_by_xpath("/html/body/div/div/main/div[9]")

try:
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body')))
    print("pop up muncul Pak")
    driver.find_element_by_xpath('//*[@id="exampleModalLong"]/div/div/div[1]/button')
    print("pop up di close")

except TimeoutException :
    print("pop up tidak muncul Pak")
    pass