Feature: Day 08

  Scenario: Number of resonant antinodes on antenna map
    Given the antenna map
        | value        |
        | T......... |
        | ...T...... |
        | .T........ |
        | .......... |
        | .......... |
        | .......... |
        | .......... |
        | .......... |
        | .......... |
        | .......... |
    Then the number of resonant antinodes is "9"

  Scenario: Number of resonant antinodes on antenna map 2
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
    Then the number of resonant antinodes is "34"