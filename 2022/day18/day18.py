import sys
from functools import reduce
import numpy as np
from math import floor, ceil


class Number:
    ids = np.arange(1000000)

    def __init__(self, val, depth):
        self.id, Number.ids = Number.ids[0], Number.ids[1:]
        self.val = val
        self.depth = depth

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)


def readlist(file):
    numbers = []
    for line in file:
        number = eval('list(' + line.rstrip() + ')')
        numbers.append(number)
    return numbers


def numberify(num, id_dict, depth=0):
    if sum([isinstance(x, list) for x in num]) == 0:
        n1, n2 = Number(num[0], depth), Number(num[1], depth)
        id_dict[n1.id] = n1
        id_dict[n2.id] = n2
        return [n1, n2]
    elif sum([isinstance(x, list) for x in num]) == 1:
        if isinstance(num[0], list):
            n = Number(num[1], depth)
            id_dict[n.id] = n
            return [numberify(num[0], id_dict, depth+1), n]
        elif isinstance(num[1], list):
            n = Number(num[0], depth)
            id_dict[n.id] = n
            return [n, numberify(num[1], id_dict, depth+1)]
    else:
        return [numberify(num[0], id_dict, depth+1), numberify(num[1], id_dict, depth+1)]  # noqa: E501


def add_nums(n1, n2, id_dict):
    new_num = [n1] + [n2]
    for n in flatten(new_num, id_dict):
        n.depth += 1
    return new_num


def flatten(li, id_dict):
    flat_li = eval('[' + str(li).replace('[', '').replace(']', '') + ']')
    return [id_dict[id] for id in flat_li]


def explode(branch, id_dict, exploded=False):
    res = []
    not_nested = True
    for el in branch:
        if isinstance(el, list):
            new, exploded = explode(el, id_dict, exploded)
            res.append(new)
            not_nested = False
        else:
            res.append(el)
    if not_nested and not exploded:
        if branch[0].depth >= 4:
            exploded = res
            n = Number(0, branch[0].depth-1)
            id_dict[n.id] = n
            res = n
    return res, exploded


def dfsplit(branch, id_dict, split=False):
    res = []
    for el in branch:
        if isinstance(el, list):
            ret, split = dfsplit(el, id_dict, split)
            res.append(ret)
        else:
            if el.val >= 10 and not split:
                l, r = el.val // 2, ceil(el.val / 2)
                d = el.depth + 1
                n1, n2 = Number(l, d), Number(r, d)
                id_dict[n1.id] = n1
                id_dict[n2.id] = n2
                res.append([n1, n2])
                split = True
            else:
                res.append(el)
    return res, split


def val_convert(num):
    if sum([isinstance(x, list) for x in num]) == 0:
        return [num[0].val, num[1].val]
    elif sum([isinstance(x, list) for x in num]) == 1:
        if isinstance(num[0], list):
            return [val_convert(num[0]), num[1].val]
        elif isinstance(num[1], list):
            return [num[0].val, val_convert(num[1])]
    else:
        return [val_convert(num[0]), val_convert(num[1])]


def increment(flat_num, exploded, id_dict):
    index_l = flat_num.index(exploded[0])
    index_r = flat_num.index(exploded[1])
    if index_l - 1 >= 0:
        flat_num[index_l - 1].val += exploded[0].val
    try:
        flat_num[index_r + 1].val += exploded[1].val
    except IndexError:
        pass


def magnitude(branch):
    if isinstance(branch, Number):
        return branch.val
    else:
        return 3 * magnitude(branch[0]) + 2 * magnitude(branch[1])


def main():
    ex_input = readlist(sys.stdin)
    id_dict = {}
    numbers = [numberify(number, id_dict) for number in ex_input]
    sum_num = numbers[0]
    for i in range(1, len(numbers)):
        sum_num = add_nums(sum_num, numbers[i], id_dict)
        while True:
            while True:
                flat_num = flatten(sum_num, id_dict)
                exp_num, exploded = explode(sum_num, id_dict)
                if exploded:
                    increment(flat_num, exploded, id_dict)
                if sum_num == exp_num:
                    break
                else:
                    sum_num = exp_num
            split_num, _ = dfsplit(exp_num, id_dict)
            if exp_num == split_num:
                break
            else:
                sum_num = split_num
    print('Question 1:\n________________________')
    print('\nResult')
    print(val_convert(sum_num))
    print('Magnitude')
    print(magnitude(sum_num))
    num_pairs = []
    results = []
    for num1 in ex_input:
        for num2 in ex_input:
            if num1 != num2:
                num_pairs.append((numberify(num1, id_dict), numberify(num2, id_dict)))  # noqa: E501
    for i in range(len(num_pairs)):
        num1, num2 = num_pairs[i]
        sum_num = add_nums(num1, num2, id_dict)
        while True:
            while True:
                flat_num = flatten(sum_num, id_dict)
                exp_num, exploded = explode(sum_num, id_dict)
                if exploded:
                    increment(flat_num, exploded, id_dict)
                if sum_num == exp_num:
                    break
                else:
                    sum_num = exp_num
            split_num, _ = dfsplit(exp_num, id_dict)
            if exp_num == split_num:
                break
            else:
                sum_num = split_num
        results.append(magnitude(sum_num))
    print('\nQuestion 2:\n________________________')
    print(max(results))


if __name__ == '__main__':
    main()
