Feature: Check store inventory

  Scenario: Retrieve store inventory
    Given the store inventory endpoint
    When sending a request to get store inventory
    Then the inventory retrieval is successful
    And the response contains the expected inventory data
