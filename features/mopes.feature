Feature: Mopes
  # Mopes detection

  Scenario: Simple mopa detection
    Given we have an initialized game with two teams
    And the team 1 has a score of 9 points
    And the team 2 has a score of 0 points
    When the team 1 scores a goal
    Then the game is over
    And the winner team is the team 1
    And the team 1 is mopper
    And the team 2 is mopped
    And the game is a mopa

  Scenario: Advanced mopa detection in sequence with multiple color balls
    Given we have an initialized game with two teams
    And the next sequence of score actions:
      | team | ball   |
      | 1    | white  |
      | 2    | white  |
      | 1    | blue   |
      | 1    | blue   |
      | 1    | blue   |
      | 1    | blue   |
      | 2    | yellow |
      | 1    | white  |
    Then the game is over
      And the winner team is the team 1
      And the team 1 is mopper
      And the team 2 is mopped
      And the game is a mopa