Feature: Login to the app

  Scenario: Login with Google
    Given I have opened the app
    When I login with Google
    Then I should be logged in successfully

  Scenario: Login with Facebook
    Given I have opened the app
    When I login with Facebook
    Then I should be logged in successfully

  Scenario: Login with Email
    Given I have opened the app
    When I login with Email
    Then I should be logged in successfully
