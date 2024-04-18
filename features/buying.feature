Feature: Manipulating with the shopping cart

    The user should be able to add products to cart from several places on the webpage and should
    be able to manipulate it e.g. remove products, change quantity of products, etc.

    Scenario: Adding featured product to cart (10)
        Given user is on the home page and the cart is empty
        When user clicks the "Add to Cart" button beneath the featured "MacBook" product
        Then the cart should contain 1 item

    Scenario: Stacking products in cart (11)
        Given user is on the home page and the cart contains 1 featured "MacBook" product
        When user clicks the "Add to Cart" button on the same featured "MacBook" product
        Then the cart should contain 2 items

    Scenario: Adding product of >1 quantity to cart from product page (12)
        Given user is on the product page and the cart is empty
        When "Qty" field is set to 2
        And "Add to Cart" button is clicked
        Then the cart should contain 2 items

    Scenario: Adding product of 0 quantity to cart from product page (13)
        Given user is on the product page and the cart is empty
        When "Qty" field is set to 0
        And "Add to Cart" button is clicked
        Then the cart should contain 0 items
        # this is how the SUT behaves, although debatable

    Scenario: Opening the cart through the button (14)
        Given user clicked on the black cart button and the cart is not empty
        When user clicks the "View cart" link in the button
        Then the cart should be opened

    Scenario: Updating quantity of product in cart (15)
        Given user is on Shopping Cart page and the cart contains 1 product of quantity 1
        When user changes the quantity of the product to 3
        And user clicks the "Update" button
        Then the cart should contain 1 product of quantity 3

    #Scenario: Removing product from cart (16)
     #   Given user is on Shopping Cart page and the cart contains 1 product
      #  When user clicks the "Remove" button
       # Then the cart should be empty

    Scenario: Proceeding to checkout from cart (17)
        Given user is on Shopping Cart page and the cart is not empty
        When user clicks the "Checkout" button
        Then the user should be redirected to the Checkout page

   #Scenario: Confirming order (18)
        #Given user is on the Checkout page
       # When user fills in the required fields
        #And clicks the "Confirm Order" button
       # Then the order should be confirmed
        #And the user should be redirected to the Order Confirmation page

    