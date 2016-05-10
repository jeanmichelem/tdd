# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
from mopes import Game, Team, Player, Ball


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


@then(u'the team {team_id:d} should have a score of {points:d} points')
def step_impl(context, team_id, points):
    if team_id == 1:
        assert context.game.score.team1 == points
    else:
        assert context.game.score.team2 == points


@given(u'we have an initialized game with two teams')
def step_impl(context):
    player_list = ['Player ' + str(i) for i in range(1,5)]
    team1 = Team(*player_list[0:2])
    team2 = Team(*player_list[2:4])
    context.game = Game(team1, team2)


@given(u'the current ball color is {ball_color}')
def step_impl(context, ball_color):
    context.game.set_current_ball(Ball.from_color(ball_color))


@when(u'the team {team_id:d} scores a goal')
def step_impl(context, team_id):
    context.game.score_goal(team_id)


@given(u'the next sequence of score actions')
def step_impl(context):
    for row in context.table:
        context.game.set_current_ball(Ball.from_color(row['ball']))
        context.game.score_goal(int(row['team']))


@given(u'the team {team:d} has a score of {points:d} points')
def step_impl(context, team, points):
    if team == 1:
        context.game.score.team1 = points
    else:
        context.game.score.team2 = points


@then(u'the game is over')
def step_impl(context):
    assert context.game.is_over()

@then(u'the winner team is the team {team:d}')
def step_impl(context, team):
    assert context.game.get_winner() == team


@then(u'the team {team:d} is mopper')
def step_impl(context, team):
    if team == 1:
        assert context.game.score.team1 == 10 \
               and context.game.score.team2 == 0
    else:
        assert context.game.score.team1 == 0 \
               and context.game.score.team2 == 10


@then(u'the team {team:d} is mopped')
def step_impl(context, team):
    if team == 1:
        assert context.game.score.team1 == 0 \
               and context.game.score.team2 == 10
    else:
        assert context.game.score.team1 == 10 \
               and context.game.score.team2 == 0


@then(u'the game is a mopa')
def step_impl(context):
    assert context.game.is_mopa()


@when(u'the team {team:d} scores an autogoal')
def step_impl(context, team):
    context.game.score_goal(team, auto_goal=True)


