Feature: Day 06

  Scenario: Guard algo
    Given the map
        | value |
        | ....#..... |
        | .........# |
        | .......... |
        | ..#....... |
        | .......#.. |
        | .......... |
        | .#..^..... |
        | ........#. |
        | #......... |
        | ......#... |
    Then the position count is "41"

