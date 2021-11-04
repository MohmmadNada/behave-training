Feature: OrangeHRM Login
    
    Scenario: Login to OrangeHRM with valid parameters
        Given I launch Chrome browser
        When I open Orange HRM Homepage 
        And Enter username "admin" and password "admin123"
        And Click on Login button
        Then User must successfully login to dashboard page
    
    Scenario Outline: Login to OrangeHRM with valid parameters
        Given I launch Chrome browser
        When I open Orange HRM Homepage 
        And Enter username "<username>" and password "<password>"
        And Click on Login button
        Then User must successfully login to dashboard page

        Examples:
            |   username  |   password  |
            |   admin     |   admin123  |
            |   admin123  |   admin     |
            # |   adminxyz  |   admin123  |
            # |   admin     |   adminxyz  |
