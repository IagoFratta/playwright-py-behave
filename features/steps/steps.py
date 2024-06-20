from behave import given, then
from features.pages.home_page import HomePage

@given('eu abro a página inicial')
def step_impl(context):
    home_page = HomePage(context.page)
    home_page.open()

@then('eu devo ver o título "{title}"')
def step_impl(context, title):
    home_page = HomePage(context.page)
    assert home_page.get_title() == title
