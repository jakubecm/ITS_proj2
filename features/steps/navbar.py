from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

@when(u'the user clicks on the category "{category}"')
def step_impl(context, category):
    category_link = context.driver.find_element(By.LINK_TEXT, category)
    category_link.click()

@then(u'the user should see all the products of the category "{category}"')
def step_impl(context, category):
    page_title = context.driver.find_element(By.CSS_SELECTOR, "h2").text
    assert category in page_title, f"No products related to {category} were found."

@when(u'the user hovers over the "{category}" category')
def step_impl(context, category):
    category_link = context.driver.find_element(By.LINK_TEXT, category)
    # Hover over the category
    ActionChains(context.driver).move_to_element(category_link).perform()

@when(u'the user clicks on the subcategory "{subcategory}"')
def step_impl(context, subcategory):
    subcategory_link = context.driver.find_elements(By.CLASS_NAME, "nav-link")
    for link in subcategory_link:
        if subcategory in link.text:
            subcategory_link = link
            break
    subcategory_link.click()

@then(u'the user should see all the products of the subcategory "{subcategory}"')
def step_impl(context, subcategory):
    active_list_elements = context.driver.find_elements(By.CLASS_NAME, "active")
    assert subcategory in active_list_elements[1].text, f"No products related to {subcategory} were found."

@when(u'the user clicks on the product "{product}"')
def step_impl(context, product):
    product_link = context.driver.find_element(By.LINK_TEXT, product)
    product_link.click()

@then(u'the user should see the details of the product "{product}"')
def step_impl(context, product):
    product_title = context.driver.find_element(By.CSS_SELECTOR, "h1").text
    assert product in product_title, f"No details of {product} were found."