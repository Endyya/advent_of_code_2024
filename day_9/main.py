import numpy as np



with open('input') as f:
    line = f.readline().rstrip('\n')

true_data = np.array(list(line[::2]))
empty_space = np.array(list(line)[1::2])

data_box = np.zeros(sum([int(i) for i in line]), dtype = int)
index = 0
ID = 0

for i, j in enumerate(line):
    j = int(j)

    if i % 2 == 0:
        data_box[index:index + j] = ID
        ID += 1
        index = index + j
    else:
        data_box[index:index + j] = -1
        index = index + j

for i, ID in enumerate(data_box[::-1]):
    first_empty = list(data_box).index(-1)
    if ID != -1 and first_empty < len(data_box) - i - 1:
        data_box[first_empty] = ID
        data_box[-i-1] = -1

first_empty = list(data_box).index(-1)
print('part 1 :', sum([i*j for i,j in enumerate(data_box[:first_empty])]))
        
        
