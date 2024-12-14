import numpy as np
from time import sleep



pos = []
speed = []

filename = 'input'

with open(filename) as f:
    for line in f:
        pos_line, speed_line = line.split(' ')
        pos_coords = pos_line.split('=')[1]
        speed_coords = speed_line.split('=')[1]
        pos.append([int(i) for i in pos_coords.split(',')])
        speed.append([int(i) for i in speed_coords.split(',')])

pos = np.array(pos)

speed = np.array(speed)

number_steps = 100

final_pos = pos + 100*speed

if filename == 'test':
    x_max = 11
    y_max = 7
else:
    x_max = 101
    y_max = 103

final_pos[:, 0] = final_pos[:, 0] % x_max
final_pos[:, 1] = final_pos[:, 1] % y_max


x_cross = x_max // 2
y_cross = y_max // 2


first_quad = final_pos[
    np.logical_and(
        final_pos[:, 0] < x_cross,
        final_pos[:, 1] < y_cross
    )
]

sec_quad = final_pos[
    np.logical_and(
        final_pos[:, 0] > x_cross,
        final_pos[:, 1] < y_cross
    )
]

third_quad = final_pos[
    np.logical_and(
        final_pos[:, 0] < x_cross,
        final_pos[:, 1] > y_cross
    )
]

fourth_quad = final_pos[
    np.logical_and(
        final_pos[:, 0] > x_cross,
        final_pos[:, 1] > y_cross
    )
]

print('part 1 :', len(first_quad) * len(sec_quad) * len(third_quad) * len(fourth_quad))

def display(pos):
    str_out = np.full(shape = (x_max, y_max), fill_value = '-')
    for coords in pos:

        str_out[*coords] = '#'
    str_out = np.transpose(str_out)
    return '\n'.join([''.join(str_out[i, :]) for i in range(str_out.shape[0])])
    

last_pos = pos.copy()

count = 0

while True and count < x_max * y_max:

    if '############' in display(last_pos):
        print('\n'*3)
        print(display(last_pos))
        print('part 2 :', count)
        break

    last_pos = last_pos + speed
    last_pos[:, 0] = last_pos[:, 0] % x_max
    last_pos[:, 1] = last_pos[:, 1] % y_max
    count += 1



    
