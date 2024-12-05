import numpy as np
order = []
updates = []
sorted_pages = []

def check_one_update(update, order):
    for i, page in enumerate(update):
        relev_order = order[order[:, 0] == page]
        if np.any(np.isin(update[i+1:], relev_order, invert = True)):
            return False
    return True

with open('input') as f:
    for line in f:
        line = line.rstrip('\n')
        if '|' in line:
            order.append(line.split('|'))
        elif ',' in line:
            updates.append(line.split(','))

order = np.array(order, dtype = int)
order = order[order[:, 0].argsort()]
updates = [[int(i) for i in line] for line in updates]

score = 0

for update in updates:
    if check_one_update(update, order):
        score += update[len(update) // 2]


print('part 1 :', score)
        


            
