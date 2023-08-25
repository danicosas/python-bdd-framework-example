from behave import given, when, then
from selenium import webdriver
from pages.duckduckgo_page import DuckDuckGoPage

@given('I am on the DuckDuckGo homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.page = DuckDuckGoPage(context.driver)
    context.page.load()

@when('I search for the term "{search_term}"')
def step_impl(context, search_term):
    context.page.enter_search(search_term)
    context.page.click_search_button()

@then('I see search results related to "{search_term}"')
def step_impl(context, search_term):
    assert search_term in context.driver.title

@then('I close the browser')
def step_impl(context):
    context.driver.quit()
