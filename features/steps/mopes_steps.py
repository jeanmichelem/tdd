# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
from mopes import Game, Team, Player

@given(u'we have an empty game')
def step_impl(context):
    context.game = Game()
    context.teams = {}

@given(u'the game score is reset')
def step_impl(context):
    context.game.reset_score()

@given(u'we have team {team_id:d} with players {player1} and {player2}')
def step_impl(context, team_id, player1, player2):
    if team_id == 1:
        context.team1 = Team(player1, player2)
    elif team_id == 2:
        context.team2 = Team(player1, player2)
    else:
        raise ValueError("team_id should be 1 or 2")

@when(u'we add the team {team_id:d} to the game')
def step_impl(context, team_id):
    if team_id == 1:
        context.game.set_team1(context.team1)
    elif team_id == 2:
        context.game.set_team2(context.team2)
    else:
        raise ValueError("team_id should be 1 or 2")


@then(u'the team {team_id} should have a score of {points:d} points')
def step_impl(context, team_id, points):
    if team_id == 1:
        assert context.game.score.team1 == points
    else:
        assert context.game.score.team2 == points
