from selenium import webdriver

driver = webdriver.Firefox(executable_path="c:\seleniumDriver\geckodriver.exe")

driver.get("https://www.amazon.es/")


print(driver.title)

assert "Amazon" in driver.title

tbx__search = driver.find_element_by_name("z")


