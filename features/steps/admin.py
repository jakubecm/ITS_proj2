import time, string, random
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'the user is logged as an admin')
def step_impl(context):
    context.driver.maximize_window()
    context.driver.get(context.base_url + "/administration")
    username = context.driver.find_element(By.ID, "input-username")
    username.send_keys("user".strip())
    password = context.driver.find_element(By.ID, "input-password")
    password.send_keys("bitnami".strip())
    
    #submit the form
    login = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    login.click()

@given(u'the user is on the admin dashboard')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.title_contains("Dashboard"))
    assert "Dashboard" in context.driver.title

@when(u'the "Catalog" sidebar item is expanded')
def step_impl(context):
    catalog = context.driver.find_element(By.XPATH, "//a[contains(text(),'Catalog')]")
    catalog.click()

@when(u'the "Products" sidebar item is clicked')
def step_impl(context):
    products = context.driver.find_element(By.XPATH, "//a[contains(text(),'Products')]")
    products.click()

@then(u'the list of all products should be seen')
def step_impl(context):
    assert "Products" in context.driver.title

@given(u'the user is on the "Products" dashboard')
def step_impl(context):
    catalog = context.driver.find_element(By.XPATH, "//a[contains(text(),'Catalog')]")
    catalog.click()
    products = context.driver.find_element(By.XPATH, "//a[contains(text(),'Products')]")
    products.click()
    WebDriverWait(context.driver, 10).until(EC.title_contains("Products"))
    assert "Products" in context.driver.title

@when(u'the "Add New" button is clicked')
def step_impl(context):
    add_new = context.driver.find_element(By.CLASS_NAME, "fa-plus")
    add_new.click()

@when(u'the product details are filled in')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.ID, "input-name-1")))
    product_name = context.driver.find_element(By.ID, "input-name-1")
    product_name.send_keys("Test Product")
    meta_tag_title = context.driver.find_element(By.ID, "input-meta-title-1")
    meta_tag_title.send_keys("Test Product")
    context.driver.find_element(By.LINK_TEXT, "Data").click()
    model = context.driver.find_element(By.ID, "input-model")
    model.send_keys("Test Model")
    price = context.driver.find_element(By.ID, "input-price")
    price.send_keys("100")
    quantity = context.driver.find_element(By.ID, "input-quantity")
    quantity.send_keys("10")
    context.driver.find_element(By.LINK_TEXT, "SEO").click()
    seo = context.driver.find_element(By.ID, "input-keyword-0-1")
    # generate a random string and send to seo key
    seo.send_keys(''.join(random.choices(string.ascii_lowercase + string.digits, k=6)))

@when(u'the "Save" button is clicked')
def step_impl(context):
    save = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    # hover over the save button
    context.driver.execute_script("arguments[0].scrollIntoView();", save)
    save.click()

@then(u'the product should be added to the list of existing products')
def step_impl(context):
    # check for alert message
    alert = context.driver.find_element(By.CLASS_NAME, "alert-success")
    assert "Success" in alert.text

@when(u'the "Edit" button is clicked for a product')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-pencil")))
    edit = context.driver.find_element(By.CLASS_NAME, "fa-pencil")
    edit.click()

@when(u'the product details are changed')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.ID, "input-name-1")))
    product_name = context.driver.find_element(By.ID, "input-name-1")
    product_name.clear()
    product_name.send_keys("Test Product Updated")

@then(u'the product should be updated in the list of existing products')
def step_impl(context):
    # check for alert message
    alert = context.driver.find_element(By.CLASS_NAME, "alert-success")
    assert "Success" in alert.text

@when(u'the checkmark for the product "Canon EOS 5D" is checked')
def step_impl(context):
    check = context.driver.find_element(By.XPATH, "//input[@value='30']")
    check.click()

@when(u'the "Delete" button is clicked')
def step_impl(context):
    delete = context.driver.find_element(By.CLASS_NAME, "fa-trash-can")
    delete.click()

@when(u'the pop up is confirmed')
def step_impl(context):
    context.driver.switch_to.alert.accept()

@then(u'the product should be removed from the list of existing products')
def step_impl(context):
    # check for alert message
    alert = context.driver.find_element(By.CLASS_NAME, "alert-success")
    assert "Success" in alert.text

@when(u'"HTC" is filled into the "Product Name" field')
def step_impl(context):
    product_name = context.driver.find_element(By.ID, "input-name")
    product_name.send_keys("HTC")

@when(u'the "Filter" button is clicked')
def step_impl(context):
    filter = context.driver.find_element(By.ID, "button-filter")
    filter.click()

@then(u'the list of products should show only the products with the name "HTC"')
def step_impl(context):
    assert "Showing 1 to 1 of 1 (1 Pages)" in context.driver.page_source
    

    