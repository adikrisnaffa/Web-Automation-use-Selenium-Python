from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.headless = True
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/select-menu")
print(driver.title)
driver.get_screenshot_as_file("screensho1.png")