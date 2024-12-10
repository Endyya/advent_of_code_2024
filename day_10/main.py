import networkx as nx
import numpy as np
import itertools as itt
import matplotlib.pyplot as mpp

data = []
with open('input') as f:
    for line in f:
        data.append(list(line.rstrip('\n')))
        
data = np.array(data, dtype = int)
profile = nx.DiGraph()

for i, j in itt.product(range(data.shape[0]), range(data.shape[1])):
    profile.add_node(f'{i},{j}', weight = data[i, j])

for i, j in itt.product(range(data.shape[0]), range(data.shape[1])):
    node_data = data[i, j]

    try:
        if node_data + 1 == data[i + 1, j]:
            profile.add_edge(f'{i},{j}', f'{i + 1},{j}')
    except IndexError:
        pass
    
    try:
        if node_data + 1 == data[i - 1, j] and i > 0:
            profile.add_edge(f'{i},{j}', f'{i - 1},{j}')            
    except IndexError:
        pass

    try:
        if node_data + 1 == data[i, j + 1]:
            profile.add_edge(f'{i},{j}', f'{i},{j + 1}')            

    except IndexError:
        pass

    try:
        if node_data + 1 == data[i, j - 1] and j > 0:
            profile.add_edge(f'{i},{j}', f'{i},{j - 1}')
    except IndexError:
        pass


node_data = dict(profile.nodes(data = True))

peaks = [node  for node in  node_data.keys() if node_data[node]['weight'] == 9]
bottom = [node  for node in  node_data.keys() if node_data[node]['weight'] == 0]

count = 0
score = 0
for bot in bottom:
    score += len(
        set(peaks).intersection(
            set(nx.descendants(profile, bot))))
    if len(set(peaks).intersection(set(nx.descendants(profile, bot)))) > 0:
        count += 1

print('part 1 :', score)
    
# pos = {}
# color = {}
# for i, j in itt.product(range(data.shape[0]), range(data.shape[1])):
#     pos[f'{i},{j}'] = (i, j)
#     color[f'{i},{j}'] = data[i, j]


# nx.draw_networkx_nodes(profile, pos, node_color = list(color.values()),
#                        node_size = 100)

# nx.draw_networkx_edges(profile, pos, node_size = 100, arrowsize = 1)

# mpp.show()



    
