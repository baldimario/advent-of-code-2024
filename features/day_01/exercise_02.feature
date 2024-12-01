Feature: Day 01

  Scenario: Second exercise Scenario
    Given I have two list "list1" and "list2"
      | value1 | value2 |
      | 3     | 4     |
      | 4     | 3     |
      | 2     | 5     |
      | 1     | 3     |
      | 3     | 9     |
      | 3     | 3     |
    When computing the counting map "count_map" from the list "list1" and "list2"
    Then the counting map "count_map" should be
      | key | value |
      | 3   | 3     |
      | 4   | 1     |
      | 2   | 0     |
      | 1   | 0     |
      | 3   | 3     |
      | 3   | 3     |
    Then the similarity score computed on the counting map "count_map" should be "31"

