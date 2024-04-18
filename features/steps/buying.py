import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

@given(u'user is on the home page and the cart is empty')
def step_impl(context):
    context.driver.get(context.base_url)
    cart_element = context.driver.find_element(By.ID, "header-cart")
    cart_button = cart_element.find_element(By.CLASS_NAME, "btn")
    assert "0" in cart_button.text

@when(u'user clicks the "Add to Cart" button beneath the featured "MacBook" product')
def step_impl(context):
    # Wait for the element to be clickable
    add_to_cart_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='product-thumb']//button[contains(@data-bs-toggle, 'tooltip')][contains(@title, 'Add to Cart')]"))
    )

    context.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    
    try:
        add_to_cart_button.click()
    except ElementClickInterceptedException:
        context.driver.execute_script("arguments[0].click();", add_to_cart_button)

@then(u'the cart should contain 1 item')
def step_impl(context):
    #wait until alert disappears
    try:
        WebDriverWait(context.driver, 4).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"))
        )
    except TimeoutException:
        pass
    cart_element = context.driver.find_element(By.ID, "header-cart")
    cart_button = cart_element.find_element(By.CLASS_NAME, "btn")
    assert "1" in cart_button.text

@given(u'user is on the home page and the cart contains 1 featured "MacBook" product')
def step_impl(context):
    context.driver.get(context.base_url)
    # add the mac
    add_to_cart_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='product-thumb']//button[contains(@data-bs-toggle, 'tooltip')][contains(@title, 'Add to Cart')]"))
    )
    cart_element = context.driver.find_element(By.ID, "header-cart")
    cart_button = cart_element.find_element(By.CLASS_NAME, "btn")
    assert "1" in cart_button.text

@when(u'user clicks the "Add to Cart" button on the same featured "MacBook" product')
def step_impl(context):
    
    add_to_cart_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='product-thumb']//button[contains(@data-bs-toggle, 'tooltip')][contains(@title, 'Add to Cart')]"))
    )

    context.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    
    try:
        add_to_cart_button.click()
    except ElementClickInterceptedException:
        context.driver.execute_script("arguments[0].click();", add_to_cart_button)

@then(u'the cart should contain 2 items')
def step_impl(context):
    #wait until alert disappears
    try:
        WebDriverWait(context.driver, 4).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"))
        )
    except TimeoutException:
        pass
    cart_element = context.driver.find_element(By.ID, "header-cart")
    cart_button = cart_element.find_element(By.CLASS_NAME, "btn")
    assert "2" in cart_button.text

@given(u'user is on the product page and the cart is empty')
def step_impl(context):
    context.driver.get(context.base_url + "/en-gb/product/macbook")
    
    # click the cart button and empty it
    cart_element = context.driver.find_element(By.ID, "header-cart")
    cart_button = cart_element.find_element(By.CLASS_NAME, "btn")
    cart_button.click()
    #click the remove
    remove_button = context.driver.find_element(By.CLASS_NAME, "btn-danger")
    remove_button.click()

    assert "0" in cart_button.text


@when(u'"Add to Cart" button is clicked')
def step_impl(context):
    cart_button = context.driver.find_element(By.ID, "button-cart")
    cart_button.click()

@when(u'"Qty" field is set to 2')
def step_impl(context):
    qty_input = context.driver.find_element(By.NAME, "quantity")
    qty_input.clear()
    qty_input.send_keys("2")

@when(u'"Qty" field is set to 0')
def step_impl(context):
    qty_input = context.driver.find_element(By.NAME, "quantity")
    qty_input.clear()
    qty_input.send_keys("0")

@then(u'the cart should contain 0 items')
def step_impl(context):
    # wait until alert disappears
    try:
        WebDriverWait(context.driver, 4).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"))
        )
    except TimeoutException:
        pass
    cart_element = context.driver.find_element(By.ID, "header-cart")
    cart_button = cart_element.find_element(By.CLASS_NAME, "btn")
    assert "0" in cart_button.text

@given(u'user clicked on the black cart button and the cart is not empty')
def step_impl(context):
    qty_input = context.driver.find_element(By.NAME, "quantity")
    qty_input.clear()
    qty_input.send_keys("1")
    cart_button = context.driver.find_element(By.ID, "button-cart")
    cart_button.click()

    #wait until alert disappears
    try:
        WebDriverWait(context.driver, 6).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"))
        )
    except TimeoutException:
        pass

    cart_element = context.driver.find_element(By.ID, "header-cart")
    cart_button = cart_element.find_element(By.CLASS_NAME, "btn")
    cart_button.click()
    

@when(u'user clicks the "View cart" link in the button')
def step_impl(context):
    view_cart_link = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
    )
    view_cart_link.click()

@then(u'the cart should be opened')
def step_impl(context):
    assert "Shopping Cart" == context.driver.title

@given(u'user is on Shopping Cart page and the cart contains 1 product of quantity 1')
def step_impl(context):
    context.driver.get(context.base_url + "/en-gb?route=checkout/cart")
    assert "Shopping Cart" == context.driver.title
    # assert only one <tr> element in <table>
    cart_table = context.driver.find_element(By.CLASS_NAME, "table-responsive")
    cart_rows = cart_table.find_elements(By.TAG_NAME, "tr")
    assert 6 == len(cart_rows)

    quantity = context.driver.find_element(By.NAME, "quantity")
    assert "1" in quantity.get_attribute("value")

@when(u'user changes the quantity of the product to 3')
def step_impl(context):
    quantity = context.driver.find_element(By.NAME, "quantity")
    quantity.clear()
    quantity.send_keys("3")

@when(u'user clicks the "Update" button')
def step_impl(context):
    update_button = context.driver.find_element(By.CLASS_NAME, "btn-primary")
    update_button.click()

@then(u'the cart should contain 1 product of quantity 3')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "table-responsive"))
    )
    cart_table = context.driver.find_element(By.CLASS_NAME, "table-responsive")
    cart_rows = cart_table.find_elements(By.TAG_NAME, "tr")
    assert 6 == len(cart_rows)

    quantity = context.driver.find_element(By.NAME, "quantity")
    assert "3" in quantity.get_attribute("value")

@given(u'user is on Shopping Cart page and the cart is not empty')
def step_impl(context):
    context.driver.get(context.base_url + "/en-gb?route=checkout/cart")
    assert "Shopping Cart" == context.driver.title
    # assert only one <tr> element in <table>
    cart_table = context.driver.find_element(By.CLASS_NAME, "table-responsive")
    cart_rows = cart_table.find_elements(By.TAG_NAME, "tr")
    assert 6 <= len(cart_rows)

@when(u'user clicks the "Checkout" button')
def step_impl(context):
    checkout_button = context.driver.find_element(By.LINK_TEXT, "Checkout")
    checkout_button.click()

@then(u'the user should be redirected to the Checkout page')
def step_impl(context):
    assert "Checkout" == context.driver.title




