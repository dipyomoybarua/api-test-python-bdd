Feature: Create users with a list

  Scenario: Successfully create a list of users
    Given a list of user data
    When sending a request to create users with the list
    Then the users are created successfully
    And the response contains the correct user details
