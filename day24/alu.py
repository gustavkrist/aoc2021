# import sys
from itertools import cycle


def alu_long(num):
    num = cycle(num)
    x = y = z = 0
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 7
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 8
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 13
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 2
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 11
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -3
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 6
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 10
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 12
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 14
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -16
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 13
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 15
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -8
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 6
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -7
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -6
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 8
    y *= x
    z += y
    w = int(next(num))
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -11
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 5
    y *= x
    z += y
    return(z)
