from behave import *

from managers.file_reader_manager import FileReaderManager
from managers.page_object_manager import PageObjectManager
from managers.webdriver_manager import WebDriverManager
from pages.duckduckgo_page import DuckDuckGoPage

def before_scenario(context, scenario):
    context.file_reader_manager = FileReaderManager()
    context.base_url = context.file_reader_manager.get_config_reader().get_value('base_url')

    context.web_driver_manager = WebDriverManager('chrome')
    context.driver = context.web_driver_manager.create_driver()

    context.page_manager = PageObjectManager(context.driver)
    duckduckgo_page = context.page_manager.get_page(DuckDuckGoPage)
    duckduckgo_page.load(context.base_url)

def after_scenario(context, scenario):
    context.web_driver_manager.quit_driver(context.driver)
