Feature: Create game
  # Basic game creation
  Scenario: Game from scratch
    Given we have an empty game
    And the game score is reset
    And we have team 1 with players player1 and player2
    And we have team 2 with players player3 and player4
    When we add the team 1 to the game
    And we add the team 2 to the game
    Then the team 1 should have a score of 0 points
    And the team 2 should have a score of 0 points
