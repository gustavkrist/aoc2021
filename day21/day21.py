import sys
from collections import Counter
from functools import lru_cache, reduce
from progressbar import ProgressBar, Bar, Percentage, ETA, FileTransferSpeed
widgets = [Percentage(), ' ', Bar('-'), ' ', ETA(), ' ', FileTransferSpeed()]


class Die:
    def __init__(self):
        self.n = 0
        self.rolls = 0

    def roll_once(self):
        self.rolls += 1
        roll = self.n + 1
        self.n = (self.n + 1) % 100
        return roll

    def roll(self):
        roll_sum = sum([self.roll_once() for i in range(3)])
        return roll_sum


class Player:
    def __init__(self, pos, die):
        self.pos = pos
        self.points = 0
        self.die = die

    def move(self):
        roll = self.die.roll()
        self.pos = (self.pos + roll) % 10
        self.points += (self.pos + 1)


class Game:
    def __init__(self, p1, p2):
        self.die = Die()
        self.p1 = Player(p1-1, self.die)
        self.p2 = Player(p2-1, self.die)

    def round(self):
        self.p1.move()
        if self.p1.points >= 1000:
            return 'break'
        self.p2.move()
        if self.p2.points >= 1000:
            return 'break'
        else:
            return 'pass'

    def sim(self):
        while True:
            action = self.round()
            if action == 'break':
                break
            else:
                pass
        min_points = min([self.p1.points, self.p2.points])
        return min_points * self.die.rolls


def read_input(f):
    p1 = int(f.readline().rstrip()[28:])
    p2 = int(f.readline().rstrip()[28:])
    return p1, p2


class WinCounter:
    w1 = 0
    w2 = 0
    # pbar = ProgressBar(widgets=widgets, maxval=786316482957124).start()

    def __init__(self):
        self.w1 = 0
        self.w2 = 0

    def winner(self):
        return max([self.w1, self.w2])

    def wincount(self):
        return self.w1 + self.w2


@lru_cache(maxsize=None)
def np(pos, roll):
    return (pos + roll) % 10


@lru_cache(maxsize=None)
def qg(p1, p2, s1=0, s2=0, going=0):
    if s1 >= 21 or s2 >= 21:
        return [1, 0] if s1 >= 21 else [0, 1]
    else:
        if going:
            return reduce(lambda x, y: [x[0] + y[0], x[1], y[1]], [list(map(
                lambda x: x*rolls[roll],
                qg(p1, np(p2, roll), s1, s2+np(p2, roll) + 1, 1-going)))
                for roll in rolls])
        else:
            return reduce(lambda x, y: [x[0] + y[0], x[1] + y[1]], [list(map(
                lambda x: x*rolls[roll],
                qg(np(p1, roll), p2, s1+np(p1, roll) + 1, s2, 1-going)))
                for roll in rolls])


def main():
    p1, p2 = read_input(sys.stdin)
    game = Game(p1, p2)
    print(game.sim())
    global rolls
    rolls = dict(Counter([sum(li) for li in [[i, j, k] for i, j, k in zip(
        [1]*9+[2]*9+[3]*9, [1, 2, 3]*9, ([1]*3+[2]*3+[3]*3)*3)]]))
    print(max(qg(p1-1, p2-1)))


if __name__ == '__main__':
    main()
