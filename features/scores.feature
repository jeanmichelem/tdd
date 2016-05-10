Feature: Scores
  # Score control and game completion
  Scenario: Basic scoring
    Given we have an initialized game with two teams
    And the current ball color is white
    When the team 1 scores a goal
    Then the team 1 should have a score of 1 points
    And the team 2 should have a score of 0 points

  Scenario: Advanced scoring with single color ball
    Given we have an initialized game with two teams
    And the next sequence of score actions:
      | team | ball   |
      | 1    | white  |
      | 2    | white  |
      | 1    | white  |
    Then the team 1 should have a score of 2 points
    And the team 2 should have a score of 1 points

  Scenario: Advanced scoring with multiple color balls
    Given we have an initialized game with two teams
    And the next sequence of score actions:
      | team | ball   |
      | 1    | white  |
      | 2    | blue   |
      | 1    | yellow |
    Then the team 1 should have a score of 0 points
    And the team 2 should have a score of 2 points

  Scenario: Game completion
    Given we have an initialized game with two teams
    And the team 1 has a score of 9 points
    And the team 2 has a score of 9 points
    When the team 1 scores a goal
    Then the game is over
    And the winner team is the team 1

  Scenario: Stop scoring when ten goals reached
    Given we have an initialized game with two teams
    And the team 1 has a score of 9 points
    And the team 2 has a score of 0 points
    When the team 1 scores a goal
    And the team 1 scores a goal
    Then the game is over
    And the team 1 should have a score of 10 points

  Scenario: Auto goal with a white ball
    Given we have an initialized game with two teams
    And the team 1 has a score of 9 points
    When the team 1 scores an autogoal
    Then the team 1 should have a score of 8 points

  Scenario: Auto goal with a yellow ball
    Given we have an initialized game with two teams
    And the team 1 has a score of 1 points
    And the current ball color is yellow
    When the team 1 scores an autogoal
    Then the team 1 should have a score of -1 points

  Scenario: Auto goal with a blue ball
    Given we have an initialized game with two teams
    And the team 1 has a score of 1 points
    And the current ball color is blue
    When the team 1 scores an autogoal
    Then the team 1 should have a score of -1 points