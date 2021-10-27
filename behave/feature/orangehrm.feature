Feature: Logo presence on OrangeHRM home Page
    Scenario: Logo chrome browser
        Given launch chrome browser
        When open orange hrm home page
        Then verify that the logo present on page
        And close browser
    