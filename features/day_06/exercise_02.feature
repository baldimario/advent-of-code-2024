Feature: Day 06

  Scenario: Guard algo loops
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
    Then the position that generate loops are "6"

