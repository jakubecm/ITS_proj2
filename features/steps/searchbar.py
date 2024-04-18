from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@given(u'the user is on the home page')
def step_impl(context):
    context.driver.get(context.base_url)
    assert "Your Store" in context.driver.title


@when(u'user enters "{keyword}" into the search bar')
def step_impl(context, keyword):
    search_input = context.driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)

@then(u'the results show products related to the "{result}"')
def step_impl(context, result):
    # Look for result in product list
    product_list = context.driver.find_elements(By.CSS_SELECTOR, ".product-thumb .description h4 a")
    found_result = any(result in product.text for product in product_list)
    assert found_result, f"No products related to {result} were found."


@given(u'the user is on the results page after searching "{product}"')
def step_impl(context, product):
    context.driver.get(context.base_url)
    search_input = context.driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys(product + Keys.RETURN)

@when(u'user clicks on a product "{product_name}" from the results')
def step_impl(context, product_name):

    xpath = f"//div[contains(@class, 'description')]/h4/a[contains(text(), '{product_name}')]"
    product_link = context.driver.find_element(By.XPATH, xpath)
    product_link.click()

@then(u'the corresponding product detail page for "{product_name}" is displayed')
def step_impl(context, product_name):
    page_title = context.driver.find_element(By.CSS_SELECTOR, "h1").text
    assert product_name in page_title, f"The product detail page for {product_name} was not displayed."


@when(u'the keyword "{keyword}" is searched with the search bar')
def step_impl(context, keyword):
    search_input = context.driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)

@when(u'user selects "Monitors" from the category filter')
def step_impl(context):
    category_filter = context.driver.find_element(By.NAME, "category_id")
    category_filter = Select(category_filter)
    category_filter.select_by_value("28")


@when(u'clicks the Search button again')
def step_impl(context):
    search_button = context.driver.find_element(By.ID, "button-search")
    search_button.click()

@then(u'a list of Samsung monitors is displayed')
def step_impl(context):
    # Look for keyword "Samsung" in product list
    product_list = context.driver.find_elements(By.CSS_SELECTOR, ".product-thumb .description h4 a")
    found_samsung = any("Samsung" in product.text for product in product_list)
    assert found_samsung, "No Samsung monitors were found in the product list."
    
    
@then(u'no other Samsung products are displayed')
def step_impl(context):
    assert "Samsung Galaxy Tab 10.1" not in context.driver.page_source


@given(u'the keyword "{keyword}" is searched with the search bar')
def step_impl(context, keyword):
    search_input = context.driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)


@when(u'user selects "Desktops" from the category filter')
def step_impl(context):
    category_filter = context.driver.find_element(By.NAME, "category_id")
    category_filter = Select(category_filter)
    category_filter.select_by_value("20")

@when(u'checkbox "Search in subcategories" is checked')
def step_impl(context):
    checkbox = context.driver.find_element(By.NAME, "sub_category")
    checkbox.click()


@when(u'the Search button is clicked')
def step_impl(context):
    search_button = context.driver.find_element(By.ID, "button-search")
    search_button.click()


@then(u'a list of iMac products is displayed')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".product-thumb .description h4 a[href*='imac']")
        found_imac = True
    except Exception as e:
        found_imac = False

    assert found_imac, "The product iMac was not found in the product list."

@given(u'the user is on the search page')
def step_impl(context):
    search_input = context.driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys()
    search_input.send_keys(Keys.RETURN)

@when(u'the user enters "intel" into the search bar')
def step_impl(context):
    search_input = context.driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys("intel")

@when(u'Search in product descriptions checkbox is checked')
def step_impl(context):
    checkbox = context.driver.find_element(By.NAME, "description")
    checkbox.click()
    search_button = context.driver.find_element(By.ID, "button-search")
    search_button.click()

@then(u'a list of products with "intel" in their description is displayed')
def step_impl(context):
    product_descriptions = context.driver.find_elements(By.CSS_SELECTOR, "#product-list .product-thumb .description p")

    # Check each description for the keyword "intel"
    found_intel = any("intel" in description.text.lower() for description in product_descriptions)
    assert found_intel, 'No products with "intel" in the description were found.'

@then(u'the results show "No products found"')
def step_impl(context):
    assert "There is no product that matches the search criteria." in context.driver.page_source

