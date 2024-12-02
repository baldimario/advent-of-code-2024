Feature: Day 02

  Scenario: Example
    Given these signals:
      | values |
      | 7 6 4 2 1 |
      | 1 2 7 8 9 |
      | 9 7 6 2 1 |
      | 1 3 2 4 5 |
      | 8 6 4 4 1 |
      | 1 3 6 7 9 |
    Then the signals safety with tolerance should be:
      | safe |
      | yes  |
      | no   |
      | no   |
      | yes  |
      | yes  |
      | yes  |
    And the number of safe signals with tolerance should be 4
