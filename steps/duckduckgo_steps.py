from behave import given, when, then
from selenium import webdriver
from pages.duckduckgo_page import DuckDuckGoPage
from managers.page_object_manager import PageObjectManager
from managers.file_reader_manager import FileReaderManager

@given('I am on the DuckDuckGo homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()

    file_reader_manager = FileReaderManager()
    base_url = file_reader_manager.get_config_reader().get_value('base_url')

    context.page_manager = PageObjectManager(context.driver)
    duckduckgo_page = context.page_manager.get_page(DuckDuckGoPage)
    duckduckgo_page.load(base_url)

@when('I search for the term "{search_term}"')
def step_impl(context, search_term):
    duckduckgo_page = context.page_manager.get_page(DuckDuckGoPage)
    duckduckgo_page.enter_search(search_term)
    duckduckgo_page.click_search_button()

@then('I see search results related to "{search_term}"')
def step_impl(context, search_term):
    assert search_term in context.driver.title

@then('I close the browser')
def step_impl(context):
    context.driver.quit()
