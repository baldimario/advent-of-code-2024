Feature: Day 05

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
    Then the position that generate loops are "6"

