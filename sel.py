from selenium.webdriver import  Chrome
driver = Chrome()

driver.get('https://www.google.com')
print(driver.title)
driver.quit()
