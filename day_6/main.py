import time
import numpy as np

lab_map = []
with open('input') as f:
    for line in f:
        lab_map.append(list(line.rstrip('\n')))

lab_map = np.array(lab_map, dtype = str)
lab_map_bak = np.array(lab_map, dtype = str)
lab_map_clean = np.array(lab_map, dtype = str)
lab_map_clean[lab_map_clean == '^' ] = '.'
lab_map_traj = np.full(shape = lab_map.shape, fill_value = 0)

current_pos = np.where(np.logical_or(
    np.logical_or(lab_map == '^', lab_map == 'v'),
    np.logical_or(lab_map == '<', lab_map == '>')))

current_dir = lab_map[current_pos][0]
current_pos = [current_pos[0][0], current_pos[1][0]]

is_exit = False
is_loop = False


while not is_exit and not is_loop:

    if current_dir == '^':
        line = lab_map[:current_pos[0] + 1, current_pos[1]]
        line = list(line[::-1])
        try:
            obstacle = line.index('#')
        except ValueError:
            obstacle = len(line)
        line[:obstacle] = ['X'] * len(range(obstacle))
        lab_map[(current_pos[0] - obstacle + 1):current_pos[0] + 1,
                current_pos[1]] = 'X'
        next_cell = lab_map_traj[
            (current_pos[0] - obstacle + 1):current_pos[0] + 1, current_pos[1]]

        if np.any(next_cell % 2 == 1):
            is_loop = True
        else:
            lab_map_traj[(current_pos[0] - obstacle + 1):current_pos[0] + 1,
                         current_pos[1]] += 1
        current_dir = '>'
        current_pos = [current_pos[0] - obstacle + 1, current_pos[1]]

    elif current_dir == '>':
        line = lab_map[current_pos[0], current_pos[1]:]
        line = list(line[::])
        try:
            obstacle = line.index('#')
        except ValueError:
            obstacle = len(line)        
        line[:obstacle] = ['X'] * len(range(obstacle))
        lab_map[current_pos[0], current_pos[1]:(current_pos[1] + obstacle)] = 'X'

        next_cell = lab_map_traj[current_pos[0],
                                 current_pos[1]:(current_pos[1] + obstacle)]
        next_cell = next_cell % 8
        if np.any((next_cell - next_cell // 4) == 4):
            is_loop = True
        else:
            lab_map_traj[current_pos[0],
                         current_pos[1]:(current_pos[1] + obstacle)] += 4

        current_dir = 'v'
        current_pos = [current_pos[0], current_pos[1] + obstacle - 1]
        
    elif current_dir == 'v':
        line = lab_map[current_pos[0]:, current_pos[1]]
        line = list(line[::])
        try:
            obstacle = line.index('#')
        except ValueError:
            obstacle = len(line)
        line[:obstacle] = ['X'] * len(range(obstacle))
        lab_map[current_pos[0]:(current_pos[0] + obstacle),
                current_pos[1]] = 'X'

        next_cell = lab_map_traj[current_pos[0]:(current_pos[0] + obstacle),
                                 current_pos[1]]
        next_cell = next_cell % 4

        if np.any((next_cell - next_cell // 2)  == 2):
            is_loop = True
        else:
            lab_map_traj[current_pos[0]:(current_pos[0] + obstacle),
                         current_pos[1]] += 2
        
        current_dir = '<'
        current_pos = [current_pos[0] + obstacle - 1, current_pos[1]]
    elif current_dir == '<':
        line = lab_map[current_pos[0], :current_pos[1] + 1]
        line = list(line[::-1])
        try:
            obstacle = line.index('#')
        except ValueError:
            obstacle = len(line)        
        line[:obstacle] = ['X'] * len(range(obstacle))
        lab_map[current_pos[0], (current_pos[1] - obstacle + 1):(current_pos[1] + 1)] = 'X'


        next_cell = lab_map_traj[current_pos[0],
                         (current_pos[1] - obstacle + 1):(current_pos[1] + 1)]
        if np.any((next_cell - next_cell // 8)  == 8):
            is_loop = True
        else:
            lab_map_traj[current_pos[0],
                         (current_pos[1] - obstacle + 1):(current_pos[1] + 1)] += 8

        
        current_dir = '^'
        current_pos = [current_pos[0], current_pos[1] - obstacle + 1]


    if (current_pos[0] in [0, lab_map.shape[0] - 1]
        or current_pos[1] in [0, lab_map.shape[1]]):
        is_exit = True



val, count = np.unique(lab_map, return_counts = True)

print('part 1 :', count[val == 'X'][0])

def is_loop(lab_map):
    
    lab_map_bak = np.array(lab_map, dtype = str)
    lab_map_clean = np.array(lab_map, dtype = str)
    lab_map_clean[lab_map_clean == '^' ] = '.'
    lab_map_traj = np.full(shape = lab_map.shape, fill_value = 0)

    current_pos = np.where(np.logical_or(
        np.logical_or(lab_map == '^', lab_map == 'v'),
        np.logical_or(lab_map == '<', lab_map == '>')))

    current_dir = lab_map[current_pos]

    current_pos = [current_pos[0][0], current_pos[1][0]]

    is_exit = False
    is_loop = False


    while not is_exit and not is_loop:

        if current_dir == '^':
            line = lab_map[:current_pos[0] + 1, current_pos[1]]
            line = list(line[::-1])
            try:
                obstacle = line.index('#')
            except ValueError:
                obstacle = len(line)
            line[:obstacle] = ['X'] * len(range(obstacle))
            lab_map[(current_pos[0] - obstacle + 1):current_pos[0] + 1,
                    current_pos[1]] = 'X'
            next_cell = lab_map_traj[
                (current_pos[0] - obstacle + 1):current_pos[0] + 1,
                current_pos[1]]

            if np.any(next_cell % 2 == 1):
                is_loop = True
            else:
                lab_map_traj[(current_pos[0] - obstacle + 1):current_pos[0] + 1,
                             current_pos[1]] += 1
            current_dir = '>'
            current_pos = [current_pos[0] - obstacle + 1, current_pos[1]]

            is_exit = current_pos[0] == 0

        elif current_dir == '>':
            line = lab_map[current_pos[0], current_pos[1]:]
            line = list(line[::])
            try:
                obstacle = line.index('#')
            except ValueError:
                obstacle = len(line)        
            line[:obstacle] = ['X'] * len(range(obstacle))
            lab_map[current_pos[0],
                    current_pos[1]:(current_pos[1] + obstacle)] = 'X'

            next_cell = lab_map_traj[current_pos[0],
                                     current_pos[1]:(current_pos[1] + obstacle)]
            next_cell = next_cell % 8
            if np.any((next_cell - next_cell // 4) == 4):
                is_loop = True
            else:
                lab_map_traj[current_pos[0],
                             current_pos[1]:(current_pos[1] + obstacle)] += 4

            current_dir = 'v'
            current_pos = [current_pos[0], current_pos[1] + obstacle - 1]

            is_exit =  current_pos[1] == lab_map.shape[1] - 1
            
        elif current_dir == 'v':
            line = lab_map[current_pos[0]:, current_pos[1]]
            line = list(line[::])
            try:
                obstacle = line.index('#')
            except ValueError:
                obstacle = len(line)
            line[:obstacle] = ['X'] * len(range(obstacle))
            lab_map[current_pos[0]:(current_pos[0] + obstacle),
                    current_pos[1]] = 'X'
            
            next_cell = lab_map_traj[current_pos[0]:(current_pos[0] + obstacle),
                                     current_pos[1]]
            next_cell = next_cell % 4

            if np.any((next_cell - next_cell // 2)  == 2):
                is_loop = True
            else:
                lab_map_traj[current_pos[0]:(current_pos[0] + obstacle),
                             current_pos[1]] += 2
        
            current_dir = '<'
            current_pos = [current_pos[0] + obstacle - 1, current_pos[1]]

            is_exit = current_pos[0] == lab_map.shape[0] - 1

        elif current_dir == '<':
            line = lab_map[current_pos[0], :current_pos[1] + 1]
            line = list(line[::-1])
            try:
                obstacle = line.index('#')
            except ValueError:
                obstacle = len(line)        
            line[:obstacle] = ['X'] * len(range(obstacle))
            lab_map[current_pos[0], (current_pos[1] - obstacle + 1):(current_pos[1] + 1)] = 'X'


            next_cell = lab_map_traj[current_pos[0],
                                     (current_pos[1] - obstacle + 1):(current_pos[1] + 1)]
            if np.any((next_cell - next_cell // 8)  == 8):
                is_loop = True
            else:
                lab_map_traj[current_pos[0],
                             (current_pos[1] - obstacle + 1):(current_pos[1] + 1)] += 8

        
            current_dir = '^'
            current_pos = [current_pos[0], current_pos[1] - obstacle + 1]

            is_exit = current_pos[1] == 0

    return is_loop


counter = 0

for i, j in np.argwhere(np.logical_and(lab_map == 'X', lab_map_bak != '^')):
    lab_map = np.copy(lab_map_bak)
    lab_map[i, j] = '#'

    if is_loop(lab_map):
        counter += 1
    
print('part 2 :', counter)
