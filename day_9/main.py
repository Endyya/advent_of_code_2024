import numpy as np

with open('input') as f:
    line = f.readline().rstrip('\n')

true_data = np.array(list(line[::2]))
empty_space = np.array(list(line)[1::2])

data_box = np.zeros(sum([int(i) for i in line]), dtype = int)
index = 0
ID = 0
        
free_chunks_size = np.array(empty_space, dtype = int)
free_chunks_indexes = np.array([sum([int(chunk) for chunk in line[:2*i+1]])
                                for i in range(len(line) // 2)], dtype = int)

data_chunks_size = np.array(true_data, dtype = int)
data_chunks_indexes = np.array([sum([int(chunk) for chunk in line[:2*i]])
                                for i in range(len(line) // 2 + 1)], dtype = int)
IDs = np.array(range(len(data_chunks_indexes)))



def make_data_box(data_size, data_ind, data_ID):
    data_box = np.full(max(data_ind) + max(data_size), fill_value = 0, dtype = int)

    for i, index in enumerate(data_ind):
        data_box[index:index+data_size[i]] = data_ID[i]
    return data_box

data_box = make_data_box(data_chunks_size, data_chunks_indexes, IDs)

print('broken part 1 :', sum([i*j for i,j in enumerate(data_box)]))


# run on ID backwards
for ID in IDs[::-1]:

    # get chunk size and indexes for this ID
    chunk_size = data_chunks_size[ID]
    chunk_index = data_chunks_indexes[ID]

    # find the lowest empty size for this chunk
    try:
        lowest_empty_size = free_chunks_size[
            np.logical_and(free_chunks_size >= chunk_size,
                           free_chunks_indexes <= chunk_index)][0]
        lowest_empty_index = free_chunks_indexes[free_chunks_size >= chunk_size][0]
    except IndexError:
        continue

    data_chunks_indexes[ID] = lowest_empty_index
    free_chunks_indexes[list(free_chunks_size).index(lowest_empty_size)] += chunk_size    
    free_chunks_size[list(free_chunks_size).index(lowest_empty_size)] -= chunk_size


data_box = make_data_box(data_chunks_size, data_chunks_indexes, IDs)

print('part 2 :', sum([i*j for i,j in enumerate(data_box)]))
