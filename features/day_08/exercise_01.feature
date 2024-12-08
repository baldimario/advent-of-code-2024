Feature: Day 08

  Scenario: Number of antinodes on antenna map
    Given the antenna map
        | value        |
        | ............ |
        | ........0... |
        | .....0...... |
        | .......0.... |
        | ....0....... |
        | ......A..... |
        | ............ |
        | ............ |
        | ........A... |
        | .........A.. |
        | ............ |
        | ............ |
    Then the number of antinodes is "14"