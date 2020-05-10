# Created by chenyuting at 2020/5/2
Feature: Health Resource

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: I want to check the service is alive
    Given health endpoint
    When I send the Get request
    Then I should get a '200' response