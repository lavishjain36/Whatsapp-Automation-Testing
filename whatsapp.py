import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()


driver.get("https://web.whatsapp.com/")

input("Please Scan Qrcode and press any key to continue:")


user = driver.find_element_by_css_selector('span[title="jenny"]')
user.click()

testinput = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
# time.sleep(10)
for i in range(10):
    testinput.send_keys("Hi.You are good")
    testinput.send_keys(Keys.RETURN)
