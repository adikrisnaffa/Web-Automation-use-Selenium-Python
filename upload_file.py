from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

#Alamat 1
driver.get("https://demoqa.com/upload-download")

#Alamat 2
# driver.get("https://gofile.io/uploadFiles")

driver.find_element_by_id("uploadFile").send_keys("C:/Users/Adikrisna/Downloads/6. Kebijakan Mutu,Keselamatan,Kesehatan Kerja,dan Lingkungan PT. Control Systems Arena Para Nusa.pdf")
#driver.find_element_by_class_name("btn btn-primary btn-lg mb-1 uploadButton").send_keys("C:/Users/Adikrisna/Downloads/6. Kebijakan Mutu,Keselamatan,Kesehatan Kerja,dan Lingkungan PT. Control Systems Arena Para Nusa.pdf")
pyautogui.write(r"C:\Users\Adikrisna\Downloads\6. Kebijakan Mutu,Keselamatan,Kesehatan Kerja,dan Lingkungan PT. Control Systems Arena Para Nusa.pdf")
