Feature: Amazon
    Scenario: Amazon show subsection in the left bar.
        When the user navigate to Amazon Home Pages
        And the user click on the first card category
        Then the left side bar should be appear in the result page.
        And the left side bar should have department text
        And the left side bar should have customer reviews text
        And the left side bar should have brand text
        And the left side bar should have price text
    Scenario: correct search result
        When the user navigate to amazon Home page
        And type iphone in search input
        And click on Search button
        Then The result page url should have iphone text