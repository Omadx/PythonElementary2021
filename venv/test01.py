from selenium import webdriver

class MyCodeModular:
    browser = "Firefox"

    def setBrowserConfig():
        driver = webdriver.Firefox(executable_path="c:\seleniumBrowserDrivers\geckodriver.exe")

    def runTest():
        driver.get("https://www.amazon.es/")
        driver.quit()


