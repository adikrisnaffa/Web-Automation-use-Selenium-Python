from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")

Text1 = driver.find_element_by_xpath("/html/body").text
print(Text1)

driver.switch_to.parent_frame()
driver.switch_to.frame("frame-middle")
Text2 = driver.find_element_by_xpath('//*[@id="content"]').text
print(Text2)
