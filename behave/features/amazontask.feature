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
    
    Scenario: Correct search result
        When the user navigate to Amazon Home page
        And type iphone in search input field
        And click on Search button
        Then The result page url should have iphone word
    
    Scenario: Create correct Amazon account
        When the user navigate to Amazon Home Page
        And click on sign in button
        And the user should be redirect to Amazon signin page
        Then The result page url should have sign word
        And the sign word should be appear
        When click on create account button
        And the user should be redirect to Amazon create account page
        Then The result page url should have register word
        When type name5 in user name field
        And type name5@gmail.com in user email field
        And type asdfgb in user password field
        And type asdfgb in user password_matcher field
        And click on continue button

    Scenario: Create Amazon account with wrong information
        When the user navigate to Amazon Home Page
        And click on sign in button
        And the user should be redirect to Amazon signin page
        # Then The result page url should have sign word
        # And the sign word should be appear
        When click on create account button
        And the user should be redirect to Amazon create account page
        Then The result page url should have register word
        When click on continue button
        Given name alert should be appear
        And email alert should be appear
        And password alert should be appear
        # user name empty 
        When the user leave user name field empty
        And type name5@gmail.com in user email field
        And type asdfgb in user password field
        And type asdfgb in user password_matcher field
        And click on continue button
        Given name alert should be appear
        # email empty 
        When type testadmin in user name field
        And the user leave user email field empty
        And type asdfgb in user password field
        And type asdfgb in user password_matcher field
        And click on continue button
        Given email alert should be appear
        # empty password
        When type testadmin in user name field
        And type testadmin@gamil.com in user email field
        And the user leave user password field empty
        And click on continue button
        Given password alert should be appear      
        # invaild email 
        When type testadmin in user name field
        And type invaildemail in user email field
        And type adminadmin in user password field
        And type adminadmin in user password_matcher field
        And click on continue button
        Given invaild email alert should be appear      
        # password with less than 6 character
        When type testadmin in user name field
        And type vaildemail@gamil.com in user email field
        And type adminadmin in user password field
        And type adminaAdmin in user password_matcher field
        And click on continue button
        Given match password alert should be appear
        # not matcher password
        When type testadmin in user name field
        And type vaildemail@gamil.com in user email field
        And type adminadmin in user password field
        And type adminaAdmin in user password_matcher field
        And click on continue button
        Given match password alert should be appear
