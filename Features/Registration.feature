Feature:Verifying Registration functionality

    @sanity @critical
    Scenario:registration with valid data
    Given:User is on registration page
    When User enters firstname 
    And User enters lastname 
    And User enters month 
    And User enters date 
    And User enters year 
    And User clicks gender
    And User enters email 
    And User enters new password 
    And User click on Sign Up
    Then User should be registered successfully

    @smoke @critical
    Scenario:registration with duplicate email 
    Given:User is on registration page
    When User enters firstname 
    And User enters lastname 
    And User enters month 
    And User enters date 
    And User enters year 
    And User clicks gender
    And User enters duplicate email 
    And User enters new password 
    And User click on Sign Up
    Then User should get duplicate email message
