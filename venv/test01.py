from selenium import webdriver

driver = webdriver.Firefox(executable_path="c:\seleniumBrowserDrivers\geckodriver.exe")

driver.get("https://www.amazon.es/")

driver.quit()

