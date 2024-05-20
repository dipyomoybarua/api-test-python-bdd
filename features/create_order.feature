Feature: Create an order

  Scenario: Successfully create an order
    Given I have a valid order data
    When I send a request to create an order
    Then the order is created successfully
    And the response status code is 200
    And the response contains the order details
