import numpy as np

data = []

def is_xmas_chunk(chunk):
    return ''.join(chunk.flat[::2]) in ['MSAMS', 'SMASM', 'SSAMM', 'MMASS']
        

with open('input') as f:
    for line in f:
        data.append(list(line.rstrip('\n')))

data = np.array(data, dtype = str)
count = 0

for i in range(data.shape[0]):
    count += ''.join(data[i, :]).count('XMAS')
    count += ''.join(data[i, :]).count('SAMX')
    count += ''.join(data[:, i]).count('XMAS')
    count += ''.join(data[:, i]).count('SAMX')
    count += ''.join(np.diagonal(data, offset = i)).count('XMAS')
    count += ''.join(np.diagonal(data, offset = i)).count('SAMX')
    count += ''.join(np.diagonal(np.fliplr(data), offset = i)).count('XMAS')    
    count += ''.join(np.diagonal(np.fliplr(data), offset = i)).count('SAMX')
    if i != 0:
        count += ''.join(np.diagonal(data, offset = -i)).count('XMAS')
        count += ''.join(np.diagonal(data, offset = -i)).count('SAMX')
        count += ''.join(np.diagonal(np.fliplr(data), offset = -i)).count('XMAS')
        count += ''.join(np.diagonal(np.fliplr(data), offset = -i)).count('SAMX')        

print('part 1 :', count)

count = 0
for i in range(data.shape[0] - 2):
    for j in range(data.shape[0] - 2):
        if is_xmas_chunk(data[i:i+3,j:j+3]):
            count += 1

print('part 2 :', count)
