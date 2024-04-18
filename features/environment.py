from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def get_driver():
    """Get Chrome/Firefox driver from Selenium Hub"""
    try:
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.ChromeOptions()
        )
    except WebDriverException:
        driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=webdriver.FirefoxOptions()
        )

    driver.implicitly_wait(15)
    return driver

# ----- BEHAVE PRESETS -----
def before_all(context):
    """Gets driver at the start of all test runs"""
    context.driver = get_driver()
    context.base_url = "http://opencart:8080"

def after_all(context):
    """Releases driver at the end of all test runs"""
    context.driver.quit()

