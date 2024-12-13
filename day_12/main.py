import numpy as np
import itertools as itt
import networkx as nx

data = []
with open('input') as f:
    for line in f:
        data.append(['-'] + list(line.rstrip('\n')) + ['-'])

outer = ['-'] * len(data[0])
data = [outer, *data,  outer]
data = np.array(data, dtype = str)

graph = nx.Graph()

for i, j in itt.product(range(1, data.shape[0] - 1),
                        range(1, data.shape[1] - 1)):
    graph.add_node(f'{i},{j}')

for i, j in itt.product(range(1, data.shape[0] - 1),
                        range(1, data.shape[1] - 1)):
    if data[i, j] == data[i - 1, j]:
        graph.add_edge(f'{i},{j}', f'{i - 1},{j}')
    if data[i, j] == data[i + 1, j]:
        graph.add_edge(f'{i},{j}', f'{i + 1},{j}')
    if data[i, j] == data[i, j - 1]:
        graph.add_edge(f'{i},{j}', f'{i},{j - 1}')
    if data[i, j] == data[i, j + 1]:
        graph.add_edge(f'{i},{j}', f'{i},{j + 1}')

score = 0
for field in nx.connected_components(graph):
    fences = 0
    for node in field:
        fences += (4 - len(nx.edges(graph, nbunch = [node])))
    score += fences * len(field)

print('part 1 :', score)

def get_edges(field: set) -> int:
    count = 0
    coordinates = {}

    # find horizontal edges
    for coord in field:
        i, j = coord.split(',')
        i = int(i)
        j = int(j)
        if i in coordinates.keys():
            coordinates[i].append(j)
            coordinates[i].sort()
        else:
            coordinates[i] = [j]

    coords = list(coordinates.keys())
    coords.sort()
    # count edges upward
    for i in coords:
        edge_started = False
        for j in coordinates[i]:
            if i - 1 in coordinates.keys() and j in coordinates[i - 1]:
                edge_started = False
            elif not edge_started and j + 1 in coordinates[i]:
                edge_started = True
                count += 1
            elif not edge_started:
                count += 1 
            elif not j + 1 in coordinates[i]:
                edge_started = False                
    # count edges downward
    for i in coords[::-1]:
        edge_started = False
        for j in coordinates[i]:
            if i + 1 in coordinates.keys() and j in coordinates[i + 1]:
                edge_started = False
            elif not edge_started and j + 1 in coordinates[i]:
                edge_started = True
                count += 1
            elif not edge_started:
                count += 1                 
            elif not j + 1 in coordinates[i]:
                edge_started = False

                
    coordinates = {}                
    # find vertical edges
    for coord in field:
        i, j = coord.split(',')
        i = int(i)
        j = int(j)
        if j in coordinates.keys():
            coordinates[j].append(i)
            coordinates[j].sort()
        else:
            coordinates[j] = [i]

    coords = list(coordinates.keys())
    coords.sort()
    for i in coords:
        edge_started = False
        for j in coordinates[i]:
            if i - 1 in coordinates.keys() and j in coordinates[i - 1]:
                edge_started = False
            elif not edge_started and j + 1 in coordinates[i]:
                edge_started = True
                count += 1
            elif not edge_started:
                count += 1
            elif not j + 1 in coordinates[i]:
                edge_started = False                

    for i in coords[::-1]:
        edge_started = False
        for j in coordinates[i]:
            if i + 1 in coordinates.keys() and j in coordinates[i + 1]:
                edge_started = False
            elif not edge_started and j + 1 in coordinates[i]:
                edge_started = True
                count += 1
            elif not edge_started:
                count += 1                
            elif not j + 1 in coordinates[i]:
                edge_started = False

    return count

score = 0
for field in nx.connected_components(graph):
    fences = 0
    score += get_edges(field) * len(field)

print('part 2 :', score)





        
    



    

