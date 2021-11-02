Feature: Amazon
    Scenario: Amazon show subsection in the left bar.
        When the user navigate to Amazon Home Page
        And the user click on the first card category
        When the user should be redirect to Amazon result Page
        Then the left side bar should be appear 
        And the left side bar should have department text
        And the left side bar should have customer reviews text
        And the left side bar should have brand text
        And the left side bar should have price text
    Scenario: correct search result
        When the user navigate to Amazon Home page
        And type iphone in search input field
        And click on Search button
        Then The result page url should have iphone word