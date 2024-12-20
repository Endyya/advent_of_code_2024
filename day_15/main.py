import numpy as np
import copy
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

        save = copy.deepcopy(self)

        if (direction == '^'
            and (type(my_map.get_component(self.coords[0] - 1, self.coords[1]))
                 == type(Empty())
                 )
            ):
            comp = my_map.get_component(self.coords[0] - 1, self.coords[1])
            comp.coords = self.coords[0], self.coords[1]
            self.coords = self.coords[0] - 1, self.coords[1]
            self.has_moved = True
        elif (direction == 'v'
            and (type(my_map.get_component(self.coords[0] + 1, self.coords[1]))
                 == type(Empty())
                 )
            ):
            comp = my_map.get_component(self.coords[0] + 1, self.coords[1])
            comp.coords = self.coords[0], self.coords[1]
            self.coords = self.coords[0] + 1, self.coords[1]
            self.has_moved = True
        elif (direction == '>'
            and (type(my_map.get_component(self.coords[0], self.coords[1] + 1))
                 == type(Empty())
                 )
            ):
            comp = my_map.get_component(self.coords[0], self.coords[1] + 1)
            comp.coords = self.coords[0], self.coords[1]
            self.coords = self.coords[0], self.coords[1] + 1
            self.has_moved = True
        elif (direction == '<'
            and (type(my_map.get_component(self.coords[0], self.coords[1] - 1))
                 == type(Empty())
                 )
            ):
            comp = my_map.get_component(self.coords[0], self.coords[1] - 1)
            comp.coords = self.coords[0], self.coords[1]
            self.coords = self.coords[0], self.coords[1] - 1
            self.has_moved = True
        elif direction == '^':
            comp = my_map.get_component(self.coords[0] - 1, self.coords[1])
            save_comp = copy.deepcopy(comp)
            try:
                comp.move('^')
                self.move('^')
            except:
                #self = save
                raise
        elif direction == 'v':
            try:
                comp = my_map.get_component(self.coords[0] + 1, self.coords[1])
                comp.move('v')
                self.move('v')
            except:
                #self = save
                raise
        elif direction == '>':
            try:
                comp = my_map.get_component(self.coords[0], self.coords[1] + 1)
                comp.move('>')
                self.move('>')
            except:
                #self = save
                raise
        elif direction == '<':
            try:
                comp = my_map.get_component(self.coords[0], self.coords[1] - 1)
                comp.move('<')
                self.move('<')
            except:
                #self = save
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

class WideBox(Object):
    def __init__(self, my_map = Map(), coords = (0, 0), *args, **kwargs):
        super().__init__(my_map = my_map, is_movable = True,
                         coords = coords, *args, **kwargs)
        self.right = RightBox(my_map = my_map, is_movable = True,
                              wide = self,
                              coords = (coords[0], coords[1] + 1),
                              *args, **kwargs)
        try:
            my_map.add_component(self.right)
        except AttributeError:
            pass

    def move(self, direction: str):

        save = copy.deepcopy(self)
        save_map = copy.deepcopy(self.my_map)
        
        if direction in ['>', '<']:
            super().move(direction = direction)
        else:
            if direction == '^':
                modif = -1
            else:
                modif = 1

            coords = self.coords
            left_comp = self.my_map.get_component(coords[0] + modif,
                                                  coords[1])
            right_comp = self.my_map.get_component(coords[0] + modif,
                                                   coords[1] + 1)
            save_left = copy.deepcopy(left_comp)
            save_right = copy.deepcopy(right_comp)
            try:
                # if the space is not empty, try to move it, then move self
                if type(left_comp) != type(Empty()):
                    left_comp.move(direction = direction)
                if not type(right_comp) in [
                        type(Empty()), type(RightBox(wide = WideBox()))]: 
                    right_comp.move(direction = direction)

                # move wide object and linked rightbox
                Object.move(self, direction = direction)
                Object.move(self.right, direction = direction)                
            except Exception as e:
                #self.my_map = save_map

                raise e

class RightBox(Object):
    def __init__(self, wide: WideBox, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wide = wide
    
    def move(self, direction: str, link = False):
        
        if direction in ['>', '<']:
            super().move(direction = direction)
        else:
            if direction == '^':
                modif = -1
            else:
                modif = 1

            coords = self.coords
            left_comp = self.my_map.get_component(coords[0] + modif,
                                                  coords[1] - 1)
            right_comp = self.my_map.get_component(coords[0] + modif,
                                                   coords[1])

            try:
                # if the space is not empty, try to move it, then move self
                if type(left_comp) != type(Empty()):
                    left_comp.move(direction = direction)
                if not type(right_comp) in [
                        type(Empty()), type(RightBox(wide = WideBox()))]: 
                    right_comp.move(direction = direction)

                # move wide object and linked rightbox
                Object.move(self, direction = direction)
                Object.move(self.wide, direction = direction)                
            except Exception as e:
                raise e
    

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
    def make_map(parse_map: np.array, part: int = 1):
        if part == 1:
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
        
        # part 2 starts here

        change_parse = np.zeros(shape = (parse_map.shape[0],
                                         parse_map.shape[1] * 2),
                                dtype = str)
        for i, j in itt.product(range(parse_map.shape[0]),
                                range(parse_map.shape[1])):
            if parse_map[i, j] == 'O':
                change_parse[i, 2 * j:2 * j + 2] = ['[', ']']
            elif parse_map[i, j] == '@':
                change_parse[i, 2 * j:2 * j + 2] = ['@', '.']
            else:
                change_parse[i, 2 * j:2 * j + 2] = parse_map[i, j]
        my_map = Map(change_parse)
        for i, j in itt.product(range(change_parse.shape[0]),
                                range(change_parse.shape[1])):
            comp = change_parse[i, j]
            if comp == '#':
                new_comp = Boundary(my_map = my_map, coords = (i, j))
            elif comp == '.':
                new_comp = Empty(my_map = my_map, coords = (i, j))
            elif comp == '@':
                new_comp = Robot(my_map = my_map, coords = (i, j))
            elif comp == 'O':
                new_comp = Box(my_map = my_map, coords = (i, j))
            elif comp == '[':
                new_comp = WideBox(my_map = my_map, coords = (i, j))

            my_map.add_component(new_comp)
        return my_map

    def display_map(self):
        comp_dict = {
            str(type(Robot())): '@',
            str(type(Empty())): ' ',
            str(type(Box())): 'O',
            str(type(Boundary())): '#',
            str(type(WideBox())): '[',
            str(type(RightBox(wide = WideBox()))): ']'}

        output = ''
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                try:
                    comp = self.get_component(i, j)
                except:
                    raise
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

for k, inst in enumerate(instructions):

    robot = my_map.get_robot()
    try:
        robot.move(inst)
    except:
        pass


score = 0
for comp in my_map.components:

    if type(comp) == type(Box()):
        score += comp.coords[0] * 100 + comp.coords[1]

print("part 1 :", score)


my_map = Map.make_map(parse_map, part = 2)

for k, inst in enumerate(instructions):
    robot = my_map.get_robot()
    save_map = copy.deepcopy(my_map)
    try:
        robot.move(inst)
    except Exception as e:
        my_map = save_map

score = 0


for comp in set(my_map.components):


    if type(comp) == type(WideBox()):
        to_add = comp.coords[0] * 100 + comp.coords[1]
        score += to_add

print('part 2 :', score)

        
