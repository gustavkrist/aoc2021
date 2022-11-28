import pprint
pprint = pprint.pprint


def star1(data):
    count = 0
    lens = [2, 3, 4, 7]
    for line in data:
        for digit in line[1]:
            if len(digit) in lens:
                count += 1
    print(count)


"bg gcdaeb aebg efabdcg abdce cafdbe fcbdeg bdacg gbd cafgd | daecb dcbae gb eabg"


def star2(data):
    total = 0
    digits_correct = {
            'abcefg': 0,
            'cf': 1,
            'acdeg': 2,
            'acdfg': 3,
            'bcdf': 4,
            'abdfg': 5,
            'abdefg': 6,
            'acf': 7,
            'abcdefg': 8,
            'abcdfg': 9
            }
    for line in data:
        output_value = ''
        digits = {len(dig): [] for dig in line[0]}
        for dig in line[0]:
            digits[len(dig)].append(dig)
        translation = {}
        one, seven, four, eight = list(digits[2][0]), list(digits[3][0]), list(digits[4][0]), list(digits[7][0])
        for i in seven:
            if i not in one:
                translation[i] = 'a'
        for digit in digits[5]:
            if one[0] in list(digit) and one[1] in list(digit):
                three = list(digit)
        for i in three:
            if i not in (one + seven + four):
                translation[i] = 'g'
                g = i
        for pos, digit in enumerate(digits[5]):
            for i in list(digit):
                if i not in (one + four + seven + [g]):
                    translation[i] = 'e'
                    twopos = pos
        for i in digits[5][twopos]:
            if i in four and i not in one:
                translation[i] = 'd'
        for i in digits[5][twopos]:
            if i not in list(translation.keys()):
                translation[i] = 'c'
        for i in one:
            if i not in list(translation.keys()):
                translation[i] = 'f'
        for i in four:
            if i not in list(translation.keys()):
                translation[i] = 'b'
        for digit in line[1]:
            digit_correct = ''.join(sorted([translation[i] for i in digit]))
            output_value += str(digits_correct[digit_correct])
        total += int(output_value)
    print(total)


def main():
    with open("input.txt") as f:
        data = []
        for line in f:
            input, output = line.rstrip().split(" | ")
            input = input.split()
            output = output.split()
            data.append([input, output])
    star1(data)
    print()
    star2(data)


if __name__ == "__main__":
    main()
