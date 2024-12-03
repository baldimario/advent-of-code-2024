Feature: Day 03

  Scenario: Monotonic increasing safe signal
    Given the memory "mem" initialized with value "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    Then the extracted pairs from memory "mem" are
      | value |
      | 2  4 |
      | 5  5 |
      | 11 8 |
      | 8  5 |
    And the result of the pairs from memory "mem" is "161"

