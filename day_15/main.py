import numpy as np
import itertools as itt
from termcolor import colored
from time import sleep

class Map():
    pass

class Object():
    def __init__(self, my_map = Map(), is_movable = False, coords = (0, 0)):
        self.my_map = my_map
        self._is_movable = is_movable
        self._has_moved = False
        self.coords = coords

    @property
    def has_moved(self):
        return self._has_moved

    @has_moved.setter
    def has_moved(self, value):
        self._has_moved = value
        
    def move(self, direction: str):
        """ direction is v, ^, < or >"""
        my_map = self.my_map
        if not self.is_movable:
            raise ValueError

        if (direction == '^'
            and (type(my_map.get_component(self.coords[0] - 1, self.coords[1]))
                 == type(Empty(my_map = self, coords = (0, 0)))
                 )
            ):
            comp = my_map.get_component(self.coords[0] - 1, self.coords[1])
            comp.coords = self.coords[0], self.coords[1]
            self.coords = self.coords[0] - 1, self.coords[1]
            self.has_moved = True
        elif (direction == 'v'
            and (type(my_map.get_component(self.coords[0] + 1, self.coords[1]))
                 == type(Empty(my_map = self, coords = (0, 0)))
                 )
            ):
            comp = my_map.get_component(self.coords[0] + 1, self.coords[1])
            comp.coords = self.coords[0], self.coords[1]
            self.coords = self.coords[0] + 1, self.coords[1]
            self.has_moved = True
        elif (direction == '>'
            and (type(my_map.get_component(self.coords[0], self.coords[1] + 1))
                 == type(Empty(my_map = self, coords = (0, 0)))
                 )
            ):
            comp = my_map.get_component(self.coords[0], self.coords[1] + 1)
            comp.coords = self.coords[0], self.coords[1]
            self.coords = self.coords[0], self.coords[1] + 1
            self.has_moved = True
        elif (direction == '<'
            and (type(my_map.get_component(self.coords[0], self.coords[1] - 1))
                 == type(Empty(my_map = self, coords = (0, 0)))
                 )
            ):
            comp = my_map.get_component(self.coords[0], self.coords[1] - 1)
            comp.coords = self.coords[0], self.coords[1]
            self.coords = self.coords[0], self.coords[1] - 1
            self.has_moved = True
        elif direction == '^':
            comp = my_map.get_component(self.coords[0] - 1, self.coords[1])
            try:
                comp.move('^')
                self.move('^')
            except:
                raise
        elif direction == 'v':
            try:
                comp = my_map.get_component(self.coords[0] + 1, self.coords[1])
                comp.move('v')
                self.move('v')
            except:
                raise
        elif direction == '>':
            try:
                comp = my_map.get_component(self.coords[0], self.coords[1] + 1)
                comp.move('>')
                self.move('>')
            except:
                raise
        elif direction == '<':
            try:
                comp = my_map.get_component(self.coords[0], self.coords[1] - 1)
                comp.move('<')
                self.move('<')
            except:
                raise            
            
    @property
    def is_movable(self):
        return self._is_movable
    

class Robot(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(is_movable = True, *args, **kwargs)

class Box(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(is_movable = True, *args, **kwargs)

class Boundary(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(is_movable = False, *args, **kwargs)

class Empty(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(is_movable = False, *args, **kwargs)

    @property
    def has_moved(self):
        return False

    @has_moved.setter
    def has_moved(self, value):
        self._has_moved = False

    


class Map():
    def __init__(self, data):
        self.data: np.array = data
        self.components: [Object] = []
        self.last_moved: [Object] = []

    def add_component(self, comp: Object):
        self.components.append(comp)

    def get_component(self, i: int, j: int):
        for comp in self.components:
            if comp.coords == (i, j):
                return comp
        raise ValueError

    def get_robot(self):
        for comp in self.components:
            if type(comp) == type(Robot(my_map = self, coords = (0, 0))):
                return comp
        raise ValueError

    @staticmethod
    def make_map(parse_map: np.array):
        my_map = Map(parse_map)
        for i, j in itt.product(range(parse_map.shape[0]),
                                range(parse_map.shape[1])):
            comp = parse_map[i, j]
            if comp == '#':
                new_comp = Boundary(my_map = my_map, coords = (i, j))
            elif comp == '.':
                new_comp = Empty(my_map = my_map, coords = (i, j))
            elif comp == '@':
                new_comp = Robot(my_map = my_map, coords = (i, j))
            elif comp == 'O':
                new_comp = Box(my_map = my_map, coords = (i, j))

            my_map.add_component(new_comp)

                                    
        return my_map

    def display_map(self):
        my_data = self.data.copy()
        comp_dict = {
            str(type(Robot())): '@',
            str(type(Empty())): ' ',
            str(type(Box())): 'O',
            str(type(Boundary())): '#'}

        output = ''
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                comp = self.get_component(i, j)
                if comp.has_moved:
                    color = 'green'
                else:
                    color = 'white'
                output += colored(comp_dict[str(type(comp))], color)
            output += '\n'

        print(output)



parse_map = []
instructions = ''

with open('input') as f:
    for line in f:
        line = line.rstrip('\n')
        if 'v' in line or '^' in line or '<' in line or '>' in line:
            instructions += line
        elif '#' in line:
            parse_map.append(list(line))

parse_map = np.array(parse_map, dtype = str)

my_map = Map.make_map(parse_map)

for inst in instructions:

    robot = my_map.get_robot()
    try:
        robot.move(inst)
    except:
        pass
    # my_map.display_map()
    # sleep(0.1)

score = 0
for comp in my_map.components:

    if type(comp) == type(Box()):
        score += comp.coords[0] * 100 + comp.coords[1]

print("part 1 :", score)



