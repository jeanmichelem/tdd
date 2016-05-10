class Score():
    def __init__(self):
        self.team1 = 0
        self.team2 = 0

    def reset(self):
        self.team1 = 0
        self.team2 = 0


class Game(object):
    def __init__(self, team1=None, team2=None):
        self.score = Score()
        self.team1 = team1
        self.team2 = team2
        self.current_ball = Ball()

    def set_team1(self, team):
        self.team1 = team

    def set_team2(self, team):
        self.team2 = team

    def reset_score(self):
        self.score.reset()

    def score_goal(self, team, auto_goal=False):
        # print 'score goal ', team
        factor = 1
        if auto_goal:
            if self.current_ball.get_points() == -1:
                factor = 2
            else:
                factor = -1
        if self.is_over():
            return  # it could raise an exception
        if team == 1:
            # print "current ball: ", self.current_ball.get_points()
            # print "factor: ", factor
            self.score.team1 += factor * self.current_ball.get_points()
            # print "team1: ", self.score.team1
            # print "team2: ", self.score.team2
        else:
            self.score.team2 += factor * self.current_ball.get_points()

    def set_current_ball(self, ball):
        self.current_ball = ball

    def is_over(self):
        return self.score.team1 == 10 or self.score.team2 == 10

    def get_winner(self):
        if self.score.team1 == 10:
            return 1
        elif self.score.team2 == 10:
            return 2

    def is_mopa(self):
        return self.score.team1 == 10 and self.score.team2 == 0 or \
               self.score.team2 == 10 and self.score.team1 == 0


class Team(object):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


class Ball(object):
    WHITE = 1
    YELLOW = -1
    BLUE = 2

    def __init__(self, points=None):
        points = points or Ball.WHITE
        self.points = points

    def get_points(self):
        return self.points

    @classmethod
    def from_color(cls, color):
        color_map = {'white': Ball.WHITE,
                     'yellow': Ball.YELLOW,
                     'blue': Ball.BLUE
                     }
        return Ball(color_map[color])


class Player(object):
    pass
