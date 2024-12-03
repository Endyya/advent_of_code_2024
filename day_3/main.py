import re

regexp = '(mul[(][0-9]+,[0-9]+[)])'

def parse_mul(exp):
    split = exp.split(',')
    first = split[0].split('(')
    number_1 = int(first[-1])
    number_2 = int(split[-1][:-1])

    return number_1 * number_2

with open('input') as f:
    lines = ''
    for line in f:
        lines += line

split_do = lines.split('do()')
split_dont = [chunk.split("don't()") for chunk in split_do]
        
matching_pattern = re.findall(regexp, lines)
print('part 1 :', sum([parse_mul(exp) for exp in matching_pattern]))

enabled = [chunk[0] for chunk in split_dont]

print('part 2 :', sum([parse_mul(exp)
                       for chunk in enabled
                       for exp in re.findall(regexp, chunk)]))
