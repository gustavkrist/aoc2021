import sys
import numpy as np
from collections import Counter
from itertools import chain
from scipy.spatial.distance import cdist
import pprint
pprint = pprint.pprint


def read_input(f):
    scanners = []
    lines = list(map(lambda x: x.split('\n'), f.read().split('\n\n')))
    for line in lines:
        line.pop(0)
        intarr = [list(map(int, el.split(','))) for el in line]
        scanners.append(np.array(intarr))
    return scanners


def dist_dict(scanner):
    scan_dists = []
    dist_done = []
    for i, p1 in enumerate(scanner):
        for j, p2 in enumerate(scanner):
            if sum(p1) != sum(p2) and {i, j} not in dist_done:
                scan_dists.append((np.linalg.norm(p1 - p2), i, j))
                dist_done.append({i, j})
    scan_dist_dict = {d: (i, j) for d, i, j in scan_dists}
    return scan_dist_dict


def base_scanner(base_dist, scan_dists):
    for i, scan_dist in enumerate(scan_dists):
        base_set = set(base_dist.keys())
        scan_set = set(scan_dist.keys())
        common_dists = base_set.intersection(scan_set)
        if len(common_dists) == 66:
            base_scan = i
    return base_scan


def common_distances(dist1, dist2):
    return set(dist1.keys()).intersection(set(dist2.keys()))


def scanner_pairs(scan_dists):
    pairs = []
    for i, scan1_dist in enumerate(scan_dists):
        for j, scan2_dist in enumerate(scan_dists):
            if {i, j} not in pairs and i != j:
                common_dists = common_distances(scan1_dist, scan2_dist)
                if len(common_dists) >= 66:
                    pairs.append({i, j})
    return pairs


def base_scan_coords(base, scan, base_dist, scan_dist):
    common_dists = common_distances(base_dist, scan_dist)
    tuple_trans = {base_dist[d]: scan_dist[d] for d in common_dists}
    common_beacons = set(chain(*[[n1, n2] for n1, n2 in tuple_trans.keys()]))
    counts = {i: Counter() for i in common_beacons}
    for (b1, b2), (s1, s2) in tuple_trans.items():
        counts[b1][s1] += 1
        counts[b1][s2] += 1
        counts[b2][s1] += 1
        counts[b2][s2] += 1
    trans = {i: max(list(dic.items()), key=lambda x: x[1])[0] for i, dic in counts.items()}  # noqa: E501
    # print(trans)
    b1, b2 = list(trans.keys())[:2]
    s1, s2 = trans[b1], trans[b2]
    base_diff = base[b1] - base[b2]
    scan_diff = scan[s1] - scan[s2]
    axis_perms = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]  # noqa: E231, E501
    scan_perms = [scan_diff[axes] for axes in axis_perms]
    for i, perm in enumerate(scan_perms):
        if np.allclose(abs(perm), abs(base_diff)):
            scan_diff = perm
            scan_rot = scan[:, axis_perms[i]]
            rot = i
    minusmask = base_diff + scan_diff != 0
    invert = np.where(minusmask, -1, 1)
    scan_invert = np.multiply(scan_rot, invert)
    coords = base[b1] + scan_invert[s1]
    return axis_perms[rot], invert, coords


def main():
    scanners = read_input(sys.stdin)
    base, scanners = scanners[0], scanners[1:]
    base_dist = dist_dict(base)
    scan_dists = [dist_dict(scanner) for scanner in scanners]
    base_scan = base_scanner(base_dist, scan_dists)
    scan_pairs = scanner_pairs(scan_dists)
    coord_dict = {}
    base_rot, base_inv, base_coords = base_scan_coords(
                base, scanners[base_scan], base_dist, scan_dists[base_scan]
                )
    coord_dict[base_scan] = base_coords
    scanners[base_scan] = scanners[base_scan][:, base_rot]
    scanners[base_scan] = base_coords - np.multiply(scanners[base_scan], base_inv)
    while len(coord_dict) < len(scanners)-1:
        for s1, s2 in scan_pairs:
            if s1 in coord_dict and s2 not in coord_dict:
                rot, inv, coords = base_scan_coords(
                        scanners[s1], scanners[s2], scan_dists[s1], scan_dists[s2]  # noqa: E501
                        )
                coord_dict[s2] = coords
                scanners[s2] = scanners[s2][:, rot]
                scanners[s2] = coords - np.multiply(scanners[s2], inv)
            elif s2 in coord_dict and s1 not in coord_dict:
                rot, inv, coords = base_scan_coords(
                        scanners[s2], scanners[s1], scan_dists[s2], scan_dists[s1]  # noqa: E501
                        )
                coord_dict[s1] = coords
                scanners[s1] = scanners[s1][:, rot]
                scanners[s1] = coords - np.multiply(scanners[s1], inv)
    pprint(coord_dict)
    print()
    beacons_based = base.copy()
    for scanner in scanners:
        beacons_based = np.r_[beacons_based, scanner]
    print(len(np.unique(beacons_based, axis=0)))
    manhat_dists = set()
    for s1, c1 in coord_dict.items():
        for s2, c2 in coord_dict.items():
            manhat_dists.add(np.sum(cdist(c1.reshape((1,3)), c2.reshape((1,3)), metric='cityblock')))
    print(max(manhat_dists))


if __name__ == "__main__":
    main()
