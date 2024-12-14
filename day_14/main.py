import numpy as np



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
