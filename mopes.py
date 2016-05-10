class Score():
    def __init__(self):
        self.reset()

    def reset(self):
        self.team1 = 0
        self.team2 = 0

class Game(object):

    def __init__(self):
        self.score = Score()
        self.team1 = None
        self.team2 = None

    def set_team1(self, team):
        self.team1 = team

    def set_team2(self, team):
        self.team2 = team

    def reset_score(self):
        self.score.reset()



class Team(object):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


class Player(object):
    pass