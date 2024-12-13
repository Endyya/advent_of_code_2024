


def get_score(a_1: int, a_2: int, 
              b_1: int, b_2: int,
              c_1: int, c_2: int) -> int:
    """System to solve :
    a_1x + b_1y = c_1
    a_2x + b_2y = c_2
    and returns corresponding score"""
    det = a_1 * b_2 - a_2 * b_1
    assert det != 0

    x = b_2 * c_1 - b_1 * c_2

    if det * x < 0 or x % det != 0:
        return 0
    
    x = x // det

    y = a_1 * c_2 - a_2 * c_1

    if det * y < 0 or y % det != 0:
        return 0

    y = y // det

    return x * 3 + y


with open('input') as f:
    score = 0
    for line in f:
        line = line.split(',')        
        if line[0].startswith('Button A:'):

            a1_but = int(line[0].split('+')[1])
            a2_but = int(line[1].split('+')[1])

        elif line[0].startswith('Button B:'):

            b1_but = int(line[0].split('+')[1])
            b2_but = int(line[1].split('+')[1])
        elif line[0].startswith('Prize:'):
            c1 = int(line[0].split('=')[1])
            c2 = int(line[1].split('=')[1])
            score += get_score(a_1 = a1_but, a_2 = a2_but,
                               b_1 = b1_but, b_2 = b2_but,
                               c_1 = c1, c_2 = c2)

print('part 1 :', score)

        
    
