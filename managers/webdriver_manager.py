from selenium import webdriver

class WebDriverManager:
    def __init__(self, browser):
        self.browser = browser

    def create_driver(self):
        if self.browser == 'chrome':
            return webdriver.Chrome()
        elif self.browser == 'firefox':
            return webdriver.Firefox()
        # Agregar más navegadores según sea necesario

    def quit_driver(self, driver):
        driver.quit()
