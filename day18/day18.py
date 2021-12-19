import sys
from itertools import chain


class SnailNum:
    def __init__(self, left, right, depth):
        self.left = left
        self.right = right
        self.depth = depth

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def __str__(self):
        return str([self.left, self.right])

    def __repr__(self):
        return str([self.left, self.right])

    def __iter__(self):
        self.curr = SnailNum.getleft
        return self

    def __next__(self):
        if self.curr == SnailNum.getleft:
            result = self.curr(self)
            self.curr = SnailNum.getright
            return result
        elif self.curr == SnailNum.getright:
            result = self.curr(self)
            self.curr = None
            return result
        else:
            raise StopIteration


def to_snailnum(number, depth=0):
    if sum([isinstance(x, list) for x in number]) == 0:
        return SnailNum(*tuple(number), depth)
    elif sum([isinstance(x, list) for x in number]) == 1:
        if isinstance(number[0], list):
            return SnailNum(*tuple([to_snailnum(number[0], depth+1), number[1]]), depth)
        elif isinstance(number[1], list):
            return SnailNum(*tuple([number[0], to_snailnum(number[1], depth+1)]), depth)
    else:
        return SnailNum(*tuple([to_snailnum(number[0], depth+1), to_snailnum(number[1], depth+1)]), depth)


def readlist(file):
    numbers = []
    for line in file:
        number = eval('list(' + line.rstrip() + ')')
        number = to_snailnum(number)
        numbers.append(number)
    return numbers


def main():
    numbers = readlist(sys.stdin)
    print(numbers)
    flat_numbers = [list(chain(*number)) for number in numbers]
    print(flat_numbers)
    # print(SnailNum.getleft(numbers[0]))


if __name__ == '__main__':
    main()
