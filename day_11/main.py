from functools import cache

def get_next_step(number_list: [int]) -> [int]:
    output = []
    for element in number_list:
        if element == 0:
            output.append(1)
        elif len(str(element)) % 2 == 0:
            elemstr = str(element)
            output.append(int(elemstr[:len(elemstr)//2]))
            output.append(int(elemstr[len(elemstr)//2:]))
        else:
            output.append(element * 2024)
                          
    return output

def find_cycle(number: int, limit: int) -> ([int], [int]):
    start = [number]
    out = []
    check_length = True
    count = 0
    count_list = []
    while check_length and count < limit:
        start = get_next_step(start)
        count += 1
        for number in start[:]:
            if number < 10:
                count_list.append(count)
                out.append(number)
                start.remove(number)
        check_length = len(start)
    return count_list, out

with open('input') as f:
    line = f.readline()

line.rstrip('\n')
line = line.split(' ')
start = [int(i) for i in line]

start = [int(i) for i in line]
data_cycle = {}

for i in range(100):
    data_cycle[i] = find_cycle(i, limit = 50000000)

@cache
def count_stones(start: int, blink: int) -> int:

    if blink == 0:
        return 1
    if start > 99 or blink < max(data_cycle[start][0]):
        count = 0
        for number in get_next_step([start]):
            count += count_stones(number, blink - 1)
        return count
    
    count = 0
    cycles = data_cycle[start][0]
    values = data_cycle[start][1]
    for cycle, value in zip(cycles, values):
        count += count_stones(value, blink - cycle)
    return count

print('part 1 :', sum([count_stones(i, 25) for i in start]))
print('part 2 :', sum([count_stones(i, 75) for i in start]))


