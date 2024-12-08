import numpy as np
import itertools as itt

data = []

with open('input') as f:
    for line in f:
        data.append(list(line.rstrip('\n')))

data = np.array(data)
empty = np.full(shape = data.shape, fill_value = '.')
antinodes = np.full(shape = data.shape, fill_value = False)

coord_sym = (2 * np.arange(data.shape[0])[:, np.newaxis]
               - np.arange(data.shape[1])[np.newaxis, :])

for freq in np.unique(data):
    if freq == '.':
        continue
    layer = np.copy(empty)
    layer[data == freq] = freq

    coord_i = np.where(data == freq)[0]
    coord_j = np.where(data == freq)[1]

    for (i1, i2), (j1, j2) in zip(itt.combinations(coord_i, 2),
                                  itt.combinations(coord_j, 2)):
        if (coord_sym[i1, i2] >= 0 and coord_sym[i1, i2] < antinodes.shape[0]
            and coord_sym[j1, j2] >= 0
            and coord_sym[j1, j2] < antinodes.shape[1]):

            antinodes[coord_sym[i1, i2], coord_sym[j1, j2]] = True

        if (coord_sym[i2, i1] >= 0
            and coord_sym[i2, i1] < antinodes.shape[0]
            and coord_sym[j2, j1] >= 0
            and coord_sym[j2, j1] < antinodes.shape[1]):
            antinodes[coord_sym[i2, i1], coord_sym[j2, j1]] = True
                        

print('part 1 :', np.count_nonzero(antinodes))

                   


