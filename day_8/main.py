import numpy as np
import itertools as itt

def check_coord(i, j, data):
    return i >= 0 and i < data.shape[0] and j >= 0 and j < data.shape[1]


def build_antinodes(data, antinodes, part = 1):

    vec_diff = (np.arange(data.shape[0])[:, np.newaxis]
                - np.arange(data.shape[1])[np.newaxis, :])
    base_point = np.arange(data.shape[0])[:, np.newaxis]

    for freq, count in zip(*np.unique(data, return_counts = True)):
        if freq == '.' or count == 1:
            continue

        coord_i = np.where(data == freq)[0]
        coord_j = np.where(data == freq)[1]

        for (i1, i2), (j1, j2) in zip(itt.combinations(coord_i, 2),
                                      itt.combinations(coord_j, 2)):
            if part == 1:
                coord_sym = vec_diff + base_point

                if check_coord(coord_sym[i1, i2], coord_sym[j1, j2], antinodes):
                    antinodes[coord_sym[i1, i2], coord_sym[j1, j2]] = True

                if check_coord(coord_sym[i2, i1], coord_sym[j2, j1], antinodes):
                    antinodes[coord_sym[i2, i1], coord_sym[j2, j1]] = True
                continue
            
            coord_anti = np.repeat(base_point, repeats = vec_diff.shape[0],
                                   axis = 1)
            while check_coord(coord_anti[i1, i2], coord_anti[j1, j2],
                              antinodes):
                antinodes[coord_anti[i1, i2], coord_anti[j1, j2]] = True
                coord_anti += vec_diff
                
            coord_anti = np.repeat(base_point, repeats = vec_diff.shape[0],
                                   axis = 1)

            while check_coord(coord_anti[i2, i1], coord_anti[j2, j1],
                              antinodes):
                antinodes[coord_anti[i2, i1], coord_anti[j2, j1]] = True
                coord_anti += vec_diff


data = []

with open('input') as f:
    for line in f:
        data.append(list(line.rstrip('\n')))

data = np.array(data)
antinodes = np.full(shape = data.shape, fill_value = False)

build_antinodes(data, antinodes, part = 1)
print('part 1 :', np.count_nonzero(antinodes))

antinodes_2 = np.full(shape = data.shape, fill_value = False)
build_antinodes(data, antinodes_2, part = 2)
print('part 2 :', np.count_nonzero(antinodes_2))
