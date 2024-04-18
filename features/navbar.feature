Feature: Listing products through the navigation bar

    Sometimes, the user may want to see all the products of some category available in the store. 
    The navigation bar provides a way to list all the products of a category or a subcategory.

    Scenario: Listing all products of a main category (7)
        Given the user is on the home page
        When the user clicks on the category "Phones & PDAs"
        Then the user should see all the products of the category "Phones & PDAs"
    
    Scenario: Listing all products of a subcategory (8)
        Given the user is on the home page
        When the user hovers over the "Components" category
        And the user clicks on the subcategory "Monitors"
        Then the user should see all the products of the subcategory "Monitors"

    Scenario: Viewing product detail from the listing page (9)
        Given the user is on the home page
        When the user clicks on the category "Phones & PDAs"
        And the user clicks on the product "HTC Touch HD"
        Then the user should see the details of the product "HTC Touch HD"