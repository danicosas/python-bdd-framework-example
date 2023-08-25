from selenium.webdriver.common.by import By

class DuckDuckGoPage:
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.searchbox_searchButton__F5Bwq')

    def __init__(self, driver):
        self.driver = driver

    def load(self, base_url):
        self.driver.get(base_url)

    def enter_search(self, search_term):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(search_term)

    def click_search_button(self):
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()
