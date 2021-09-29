from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

def driverInit(url):

    try:
        # driver.get_screenshot_as_file("1.png")
        driver.get(url)
        time.sleep(5)
        driver.save_screenshot("2.png")
        time.sleep(2)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

