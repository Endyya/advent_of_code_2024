

def parse(line):
    number, elements = line.split(':')
    number = int(number)
    elements = elements.strip('\n ')
    elements = elements.split(' ')
    elements = [int(n) for n in elements]
    return number, elements

def is_good(n, lon, part = 1):
    if len(lon) > 1:
        test_sum = is_good(n - lon[-1], lon[:-1], part = part)
        test_prod = (not n % lon[-1]
                     and is_good(n // lon[-1], lon[:-1], part = part))
        test_part_2 = False
        if part == 2:
            remain = n % 10**len(str(lon[-1]))
            quo = n // 10 ** len(str(lon[-1]))
            test_part_2 = (remain == lon[-1]
                           and is_good(quo, lon[:-1], part = 2))
        return test_sum or test_prod or test_part_2
    elif len(lon) == 1:
        return lon[0] == n

score = 0
score_2 = 0
with open('input') as f:
    for line in f:
        n, lon = parse(line)
        if is_good(n, lon):
            score += n
            score_2 += n
        elif is_good(n, lon, part = 2):
            score_2 += n
                     

print('part 1 :', score)
print('part 2 :', score_2)
