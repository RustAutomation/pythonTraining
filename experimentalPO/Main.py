from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriverPython\\chromedriver.exe")
print(type(driver))
driver.get("https://www.google.com/")
myPageTitle = driver.title
print(myPageTitle)
assert "Google" in myPageTitle
input = driver.find_element_by_xpath("//input[@title='Поиск']")
input.send_keys("123")
driver.quit()
