Feature: Day 03

  Scenario: Monotonic increasing safe signal
    Given the memory "mem" initialized with value "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    Then the extracted enabled pairs from memory "mem" are
      | value |
      | 2  4 |
      | 8  5 |
    And the result of the enabled pairs from memory "mem" is "48"

