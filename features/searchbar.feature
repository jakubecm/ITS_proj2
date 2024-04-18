
Feature: Searching for products with the search bar

    As a customer, I want to be able to effectively search for products through the search bar or search page so that I can find the products I am looking for.
    I also want to be able to filter the products by category so that I can find the products I am looking for more easily.
        

    Scenario Outline: Searching a keyword with the search bar (1)
        Given the user is on the home page
        When user enters "<keyword>" into the search bar
        Then the results show products related to the "<keyword>"
        Examples: Products
            | keyword  | result       |
            | HTC      | HTC Touch HD |
            | iPhone   | iPhone       | 
            | Nikon    | Nikon D300   |

    Scenario: Opening product detail after searching (2)
        Given the user is on the results page after searching "HTC"
        When user clicks on a product "HTC Touch HD" from the results
        Then the corresponding product detail page for "HTC Touch HD" is displayed
        
    Scenario: Searching and filtering a product by category (3)
        Given the user is on the home page
        When the keyword "Samsung" is searched with the search bar
        And user selects "Monitors" from the category filter
        And clicks the Search button again
        Then a list of Samsung monitors is displayed
        But no other Samsung products are displayed

    Scenario: Searching and filtering including a subcategory (4)
        Given the keyword "iMac" is searched with the search bar
        When user selects "Desktops" from the category filter
        And checkbox "Search in subcategories" is checked
        And the Search button is clicked
        Then a list of iMac products is displayed
    
    Scenario: Searching for a product that has a keyword in description (5)
        Given the user is on the search page
        When user enters "intel" into the search bar
        And Search in product descriptions checkbox is checked
        Then a list of products with "intel" in their description is displayed
    
    Scenario: Searching for a product that doesn't exist (6)
        When user enters "qwerty" into the search bar
        Then the results show "No products found"
    
