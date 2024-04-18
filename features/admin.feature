Feature: Managing goods and its availability in the eshop
        
    Scenario: Viewing the Product List (19)
        Given the user is logged as an admin
        And the user is on the admin dashboard
        When the "Catalog" sidebar item is expanded
        And the "Products" sidebar item is clicked
        Then the list of all products should be seen

    Scenario: Adding a new product (20)
        Given the user is logged as an admin
        And the user is on the "Products" dashboard
        When the "Add New" button is clicked
        And the product details are filled in
        And the "Save" button is clicked
        Then the product should be added to the list of existing products

    Scenario: Editing an existing product (21)
        Given the user is logged as an admin
        And the user is on the "Products" dashboard
        When the "Edit" button is clicked for a product
        And the product details are changed
        And the "Save" button is clicked
        Then the product should be updated in the list of existing products

    Scenario: Deleting an existing product (22)
        Given the user is logged as an admin
        And the user is on the "Products" dashboard
        When the checkmark for the product "Canon EOS 5D" is checked
        And the "Delete" button is clicked
        And the pop up is confirmed
        Then the product should be removed from the list of existing products

    Scenario: Filtering in the products list (23)
        Given the user is logged as an admin
        And the user is on the "Products" dashboard
        When "HTC" is filled into the "Product Name" field
        And the "Filter" button is clicked
        Then the list of products should show only the products with the name "HTC"

    #Scenario: Updating product availability (24)
     #   Given the user is logged as an admin
      #  And the user is on the "Products" dashboard
       # When the "Edit" button is clicked for a product
        #And the "Quantity" field on the "Data" tab is changed
        #And the "Save" button is clicked
        #Then the product availability should be updated
