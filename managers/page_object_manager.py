class PageObjectManager:
    def __init__(self, driver):
        self.driver = driver
        self.page_cache = {}

    def get_page(self, page_class):
        if page_class not in self.page_cache:
            self.page_cache[page_class] = page_class(self.driver)
        return self.page_cache[page_class]
