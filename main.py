import numpy as np

with open('input') as f:
    data = np.genfromtxt(f, dtype = int)

column1 = data[:, 0]
column2 = data[:, 1]

column1.sort()
column2.sort()
    
print('part 1 :', sum(np.abs(column1 - column2)))

s_score = 0

for number in column1:
    s_score += list(column2).count(number) * number

print('part 2 :', s_score)
