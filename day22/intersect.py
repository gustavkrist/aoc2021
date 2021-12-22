import sys


state, coords = sys.stdin.readline().rstrip().split(' ')
s1, s2 = state.split(',')
# x1, x2, a1, a2 = list(map(int, coords.split(',')))
# x_range = x2-x1
# a_range = a2-a1
# if x2 - a1 < 0 or x1 - a2 > 0:
#     print('Does not intersect')
#     print(f'{x1}..{x2}, {a1}..{a2}')
# elif x1 - a1 > 0 and x2 - a2 > 0:
#     print('Intersect from left')
#     print(f'{a1}..{a2}, {a2+1}..{x2}')
# elif x1 - a1 < 0 and x2 - a2 < 0:
#     print('Intersect from right')
#     print(f'{s1}: {x1}..{a1-1}, {s2}: {a1}..{a2}')
# elif x1 - a1 < 0 and x2 - a2 > 0:
#     print('Middle intersection')
#     print(f'{s1}: {x1}..{a1-1}, {s2}: {a1}..{a2}, {s1}: {a2+1}..{x2}')

x1, x2, y1, y2, z1, z2, a1, a2, b1, b2, c1, c2 = \
        list(map(int, coords.split(',')))
if (x2 - a1 < 0 or x1 - a2 > 0) or (y2 - b1 < 0 or y1 - b2 > 0) \
        or (z2 - c1 < 0 or z1 - c2 > 0):
    print("No intersection")
else:

    # Checking x
    if x1 - a1 > 0 and x2 - a2 > 0:
        new_x1 = a2+1
        x_type = 'n'
    elif x1 - a1 < 0 and x2 - a2 < 0:
        new_x2 = a1-1
        x_type = 'p'
    elif a1 < x1 and x2 < a2:
        x_spanned = True
        x_type = 's'
    else:
        x_midl = a1-1
        x_midr = a2+1
        x_type = 'm'

    # Checking y
    if y1 - b1 > 0 and y2 - b2 > 0:
        new_y1 = b2 + 1
        y_type = 'n'
    elif y1 - b1 < 0 and y2 - b2 < 0:
        new_y2 = b1 - 1
        y_type = 'p'
    elif b1 < y1 and y2 < b2:
        y_type = 's'
    else:
        y_midl = b1 - 1
        y_midr = b2 + 1
        y_type = 'm'

    # Checking z
    if z1 - c1 > 0 and z2 - c2 > 0:
        z_type = 'n'
    elif z1 - c1 < 0 and z2 - c2 < 0:
        z_type = 'p'
    elif c1 < z1 and z2 < c2:
        z_type = 's'
    else:
        z_type = 'm'

    print(x_type, y_type, z_type)
