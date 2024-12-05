import numpy as np
import itertools as itt
import networkx as nx
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

score_1 = 0


for update in updates:
    if check_one_update(update, order):
        score_1 += update[len(update) // 2]

to_sort = list(set(order[:, 0]).union(set(order[:, 1])))

print('part 1 :', score_1)


my_graph = nx.DiGraph()

all_values = set(order[:, 0]).union(set(order[:, 1]))
my_graph.add_nodes_from(all_values)
for order_node in order:
    my_graph.add_edge(order_node[1], order_node[0])
# for val_1, val_2, val_3 in itt.combinations(all_values, r = 3):
#     if (my_graph.has_edge(val_1, val_2)
#         and my_graph.has_edge(val_2, val_3)
#         and my_graph.has_edge(val_1, val_3)):
#         my_graph.remove_edge(val_1, val_3)
#     if (my_graph.has_edge(val_1, val_3)
#         and my_graph.has_edge(val_3, val_2)
#         and my_graph.has_edge(val_1, val_2)):
#         my_graph.remove_edge(val_1, val_2)
#     if (my_graph.has_edge(val_2, val_3)
#         and my_graph.has_edge(val_3, val_1)
#         and my_graph.has_edge(val_2, val_1)):
#         my_graph.remove_edge(val_2, val_1)
#     if (my_graph.has_edge(val_2, val_1)
#         and my_graph.has_edge(val_1, val_3)
#         and my_graph.has_edge(val_2, val_3)):
#         my_graph.remove_edge(val_2, val_3)
#     if (my_graph.has_edge(val_3, val_1)
#         and my_graph.has_edge(val_1, val_2)
#         and my_graph.has_edge(val_3, val_2)):
#         my_graph.remove_edge(val_3, val_2)
#     if (my_graph.has_edge(val_3, val_2)
#         and my_graph.has_edge(val_2, val_1)
#         and my_graph.has_edge(val_3, val_1)):
#         my_graph.remove_edge(val_3, val_1)

        
def sort_update(graph, update):
    if len(update) <= 1:
        return update[:]
    higher = set(graph.successors(update[0])).intersection(set(update))
    lower = set(graph.predecessors(update[0])).intersection(set(update))
    return (sort_update(graph, list(higher))
            + [update[0]]
            + sort_update(graph, list(lower)))
score_2 = 0        
        
for update in updates:
    sort = sort_update(my_graph, update)
    if update != sort:
        score_2 += sort[len(sort) // 2]
    else:
        print('bad :', update)





print('part 2 :', score_2)
        


            
