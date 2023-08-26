from behave import given, when, then
from pages.duckduckgo_page import DuckDuckGoPage

@given('I am on the DuckDuckGo homepage')
def step_impl(context):
    duckduckgo_page = context.page_manager.get_page(DuckDuckGoPage)
    duckduckgo_page.load(context.base_url)

@when('I search for the term "{search_term}"')
def step_impl(context, search_term):
    duckduckgo_page = context.page_manager.get_page(DuckDuckGoPage)
    duckduckgo_page.enter_search(search_term)
    duckduckgo_page.click_search_button()

    context.search_term = search_term

@then('I see search results related to the search term')
def step_impl(context):
    assert context.search_term in context.driver.title
