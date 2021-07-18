Feature: Login Action

  Scenario: As a guest I want to enter login page
     Given I opened browser
      When I enter page URL
      Then I see the Login page

  Scenario: As a guest I want to see Cookie Policy pop-up
      Given I opened browser
      When I enter page URL
      Then I see Cookie Policy pop-up
