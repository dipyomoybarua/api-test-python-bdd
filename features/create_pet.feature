Feature: Create a pet

  Scenario: Successfully create a pet
    Given I have a valid pet data
    When I send a request to create a pet
    Then the pet is created successfully
    And the response status code is 200
    And the response contains the pet name and status
