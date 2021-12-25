from alu import alu_long
from functools import lru_cache


@lru_cache(maxsize=None)
def s1(w, z):
    z *= 26
    z = w + 7
    return z


@lru_cache(maxsize=None)
def s2(w, z):
    z *= 26
    z += w + 8
    return z


@lru_cache(maxsize=None)
def s3(w, z):
    z *= 26
    z += w + 2
    return z


@lru_cache(maxsize=None)
def s4(w, z):
    z *= 26
    z += w + 11
    return z


@lru_cache(maxsize=None)
def s5(w, z):
    if z % 26 - 3 == w:
        z //= 26
    else:
        z //= 26
        z *= 26
        z += w + 6
    return z


@lru_cache(maxsize=None)
def s6(w, z):
    z *= 26
    z += w + 12
    return z


@lru_cache(maxsize=None)
def s7(w, z):
    z *= 26
    z += w + 14
    return z


@lru_cache(maxsize=None)
def s8(w, z):
    if z % 26 - 16 == w:
        z //= 26
    else:
        z //= 26
        z *= 26
        z += w + 13
    return z


@lru_cache(maxsize=None)
def s9(w, z):
    z *= 26
    z += w + 15
    return z


@lru_cache(maxsize=None)
def s10(w, z):
    if z % 26 - 8 == w:
        z //= 26
    else:
        z //= 26
        z *= 26
        z += w + 10
    return z


@lru_cache(maxsize=None)
def s11(w, z):
    if z % 26 - 12 == w:
        z //= 26
    else:
        z //= 26
        z *= 26
        z += w + 6
    return z


@lru_cache(maxsize=None)
def s12(w, z):
    if z % 26 - 7 == w:
        z //= 26
    else:
        z //= 26
        z *= 26
        z += w + 10
    return z


@lru_cache(maxsize=None)
def s13(w, z):
    if z % 26 - 6 == w:
        z //= 26
    else:
        z //= 26
        z *= 26
        z += w + 8
    return z


@lru_cache(maxsize=None)
def s14(w, z):
    if z % 26 - 11 == w:
        z //= 26
    else:
        z //= 26
        z *= 26
        z += w + 5
    return z


nums = []

for a in range(1, 10):
    for b in range(a, 10):
        for c in range(b, 10):
            for d in range(c, 10):
                for e in range(d, 10):
                    for f in range(e, 10):
                        for g in range(f, 10):
                            for h in range(g, 10):
                                for i in range(h, 10):
                                    for j in range(i, 10):
                                        for k in range(j, 10):
                                            for l in range(k, 10):
                                                for m in range(l, 10):
                                                    for n in range(m, 10):
                                                        nums.append(''.join(list((map(str, [a,b,c,d,e,f,g,h,i,j,k,l,m,n])))))

print(len(nums))


def alu_short(num):
    funcs = [s1, s2, s3, s4, s5, s6, s7, s8,
             s9, s10, s11, s12, s13, s14]
    z = 0
    for w, f in zip(num, funcs):
        z = f(int(w), z)
    return z


# valid = []
# invalid = []
# for num in range(99999999999999, 0, -1):
#     strnum = str(num)
#     if '0' not in strnum:
#         z = alu_short(strnum)
#         if z == 0:
#             print(strnum)
#             break
#         else:
#             print(num)
#             # valid.append(int(num))
#         # else:
#             # invalid.append(int(num))

# print(len(valid))
# print(len(invalid))
