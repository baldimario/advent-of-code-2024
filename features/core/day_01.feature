Feature: Day 01

  Scenario: First exercise scenario
    Given I have two list "list1" and "list2"
      | value1 | value2 |
      | 3     | 4     |
      | 4     | 3     |
      | 2     | 5     |
      | 1     | 3     |
      | 3     | 9     |
      | 3     | 3     |
    When sorting the list "list1"
    And sorting the list "list2"
    And computing the list "comp_list" comparing "list1" and "list2"
    Then the list "list1" should be
      | value |
      | 1     |
      | 2     |
      | 3     |
      | 3     |
      | 3     |
      | 4     |
    And the list "list2" should be
      | value |
      | 3     |
      | 3     |
      | 3     |
      | 4     |
      | 5     |
      | 9     |
    And the list "comp_list" should be
      | value |
      | 2     |
      | 1     |
      | 0     |
      | 1     |
      | 2     |
      | 5     |
    And the sum of the list "comp_list" should be "11"

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
