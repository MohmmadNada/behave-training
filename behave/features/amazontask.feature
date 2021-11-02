Feature: Amazon show subsection in the left bar.
    Scenario: Amazon show subsection in the left bar.
        When the user navigate to Amazon home page
        And the user click on the first card category
        Then the left side bar should be appear
        And the left side bar should have department text
        And the left side bar should have customer reviews text
        And the left side bar should have brand text
        And the left side bar should have price text
    