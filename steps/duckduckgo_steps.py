import json
import os
from behave import given, when, then, step, use_step_matcher
from pages.duckduckgo_page import DuckDuckGoPage
from utils.wait_utility import WaitUtility

# Ruta para el archivo JSON en la carpeta "data"
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'search_data.json')

with open(file_path) as json_file:
    search_data = json.load(json_file)

# ... (otros pasos)

use_step_matcher("re")  # Usamos expresiones regulares para hacer coincidir los pasos

@given('I am on the DuckDuckGo homepage')
def step_impl(context):
    duckduckgo_page = context.page_manager.get_page(DuckDuckGoPage)
    duckduckgo_page.load(context.base_url)

@when('I search for the term "(?P<SearchTerm>.+)"')
def step_impl(context, SearchTerm):
    for search in search_data['searches']:
        if search['term'] == SearchTerm:
            duckduckgo_page = context.page_manager.get_page(DuckDuckGoPage)
            duckduckgo_page.enter_search(search['term'])
            duckduckgo_page.click_search_button()

            context.search_term = search['term']
            context.expected_result = search['expected_result']

@then('I see search results related to the term "(?P<SearchTerm>.+)"')
def step_impl(context, SearchTerm):
    assert context.search_term in context.driver.title
    assert context.expected_result in context.driver.title

@step('I capture a screenshot')
def step_impl(context):
    screenshot_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'screenshots')
    screenshot_file = os.path.join(screenshot_dir, f'{context.scenario.name}.png')
    context.driver.save_screenshot(screenshot_file)
