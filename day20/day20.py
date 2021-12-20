import sys
import numpy as np
from progressbar import ProgressBar, Bar, Percentage, ETA, FileTransferSpeed
widgets = [Percentage(), ' ', Bar('-'), ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets)


def read_input(f):
    algorithm = ''
    for line in f:
        if line == '\n':
            break
        else:
            algorithm += line.rstrip()
    image = [list(line.rstrip()) for line in f]
    image = np.array(image)
    height, width = image.shape
    col = np.full((height, 52), '.')
    row = np.full((52, width+104), '.')
    image = np.c_[np.c_[col, image], col]
    image = np.r_[np.r_[row, image], row]
    return algorithm, image


def sim(img, alg, iter):
    out = img.copy()
    h, w = out.shape
    for i in range(1, h-1):
        for j in range(1, w-1):
            slice = img[[[i-1], [i], [i+1]], [j-1, j, j+1]]
            bit = ''.join(['0' if pix == '.' else '1' for pix in slice.reshape((9))])
            index = eval('0b' + bit)
            out[i, j] = alg[index]
    if alg[0] == '#' and alg[-1] == '.':
        for r in [0, -1]:
            for j in range(w):
                if out[r, j] == '.':
                    out[r, j] = '#'
                else:
                    out[r, j] = '.'
        for c in [0, -1]:
            for i in range(1, h-1):
                if out[i, c] == '.':
                    out[i, c] = '#'
                else:
                    out[i, c] = '.'
    return out


def main():
    alg, img = read_input(sys.stdin)
    uni, counts = np.unique(img, return_counts=True)
    print(counts[np.where(uni == '#')])
    for i in pbar(range(50)):
        img = sim(img, alg, i)
    uni, counts = np.unique(img, return_counts=True)
    print()
    print(counts[np.where(uni == '#')])


if __name__ == '__main__':
    main()
