Feature: Temporary feature

  Scenario: Check that the dictionary works
    Given I have a dictionary "myDictionary"
    When the dictionary "myDictionary" has the "key" key with the value "val"
    Then the dictionary "myDictionary" should not have the "yek" key inside
    And the dictionary "myDictionary" should have the "key" key inside with the value "val"

