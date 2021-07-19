Feature: Login Action

  Scenario: As a guest I want to enter login page
     Given I opened browser
      When I enter page URL
      Then I see the Login page

  Scenario: As a guest I want to see Cookie Policy pop-up
     Given I opened browser
      When I enter page URL
      Then I see Cookie Policy pop-up

  Scenario: As a guest I want to accept Cookie Policy
     Given I enter page URL
      When I click accept All Cookie Policy button
      Then I see the Login page

  Scenario: As a guest I want to enter Get the app on Google play page
     Given I opened browser
      When I enter page URL
      Then I see Google Play integration link
       And I see Google Play integration link is clickable

  Scenario: As a guest I want to enter Forgot password page
     Given I enter page URL
      When I click Forgot password button
      Then I see the Forgot password page

  Scenario: As a guest I want to enter Sign up page
     Given I enter page URL
      When I click Sign up button
      Then I see the Sign up page

  Scenario: As a guest I want to enter Sign up with Facebook page
     Given I enter page URL
      When I click Log in with Facebook button
      Then I see the Log in with Facebook page
