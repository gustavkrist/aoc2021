def star1(data):
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    corrupted = []
    for line in data:
        brackets = []
        i = -1
        for pos, char in enumerate(line):
            if char in opening:
                i += 1
                if i >= len(brackets):
                    brackets.insert(i, [])
                brackets[i].append(char)
            elif char in closing:
                try:
                    index = closing.index(char)
                    openchar = opening[index]
                    brackets[i].remove(openchar)
                    i -= 1
                except ValueError:
                    corrupted.append(char)
                    break
    total = 0
    values = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for char in corrupted:
        total += values[char]
    print(total)


def star2(data):
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    values = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for linenum, line in enumerate(data):
        brackets = []
        i = -1
        corrupted = False
        for pos, char in enumerate(line):
            if char in opening:
                i += 1
                if i >= len(brackets):
                    brackets.insert(i, [])
                brackets[i].append(char)
            elif char in closing:
                try:
                    index = closing.index(char)
                    openchar = opening[index]
                    brackets[i].remove(openchar)
                    i -= 1
                except ValueError:
                    corrupted = True
                    break
        if not corrupted:
            closestr = ''
            for li in reversed(brackets):
                for char in reversed(li):
                    index = opening.index(char)
                    closechar = closing[index]
                    closestr += closechar
            linescore = 0
            for char in closestr:
                linescore *= 5
                linescore += values[char]
            scores.append(linescore)
    sorted_scores = sorted(scores)
    print(sorted_scores[len(scores) // 2])


def main():
    with open("input.txt") as f:
        data = [line.rstrip() for line in f]
    star1(data)
    print()
    star2(data)


if __name__ == "__main__":
    main()
