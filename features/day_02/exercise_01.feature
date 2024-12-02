Feature: Day 02

  Scenario: Monotonic increasing safe signal
    Given the signal "signal_safe_1"
      | value |
      | 1     |
      | 2     |
      | 3     |
      | 4     |
    Then the signal "signal_safe_1" should be safe

  Scenario: Monotonic decreasing safe signal
    Given the signal "signal_safe_2"
      | value |
      | 5     |
      | 4     |
      | 3     |
      | 2     |
    Then the signal "signal_safe_2" should be safe

  Scenario: Non-monotonic safe signal
    Given the signal "signal_unsafe_1"
      | value |
      | 1     |
      | 2     |
      | 3     |
      | 2     |
    Then the signal "signal_unsafe_1" should not be safe

  Scenario: Non safe signal with a big jump
    Given the signal "signal_unsafe_2"
      | value |
      | 1     |
      | 2     |
      | 7     |
      | 8     |
    Then the signal "signal_unsafe_2" should not be safe

  Scenario: Example
    Given these signals:
      | values |
      | 7 6 4 2 1 |
      | 1 2 7 8 9 |
      | 9 7 6 2 1 |
      | 1 3 2 4 5 |
      | 8 6 4 4 1 |
      | 1 3 6 7 9 |
    Then the signals safety should be:
      | safe |
      | yes  |
      | no   |
      | no   |
      | no   |
      | no   |
      | yes  |
    And the number of safe signals should be 2
