'''
Rover module
'''
from grid import Grid


class Rover:
    '''
    Rover class.
    '''

    def __init__(self, position: str, grid: Grid):
        '''
        Constructor.
        '''
        self.__raw_x_position, self.__raw_y_position, self.__direction = tuple(
            position.split(' ')
        )
        self.x_position = int(self.__raw_x_position)
        self.y_position = int(self.__raw_y_position)
        if self.__direction not in ('N', 'E', 'S', 'W'):
            raise ValueError('Invalid direct set for the rover.')
        self.direction = self.__direction
        self.grid = grid

    def turn_left(self):
        '''
        Turn the rover left.
        '''
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        '''
        Turn the rover right.
        '''
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'

    def move(self):
        '''
        Move the rover on the plateau grid.
        '''
        if self.direction == 'N':
            if self.y_position >= self.grid.y_right_top_coordinate:
                raise ValueError('Invalid move: rover can not go overboard')
            self.y_position += 1
        elif self.direction == 'E':
            if self.x_position >= self.grid.x_right_top_coordinate:
                raise ValueError('Invalid move: rover can not go overboard')
            self.x_position += 1
        elif self.direction == 'S':
            if self.y_position <= self.grid.y_left_bottom_coordinate:
                raise ValueError('Invalid move: rover can not go overboard')
            self.y_position -= 1
        elif self.direction == 'W':
            if self.x_position <= self.grid.x_left_bottom_coordinate:
                raise ValueError('Invalid move: rover can not go overboard')
            self.x_position -= 1

    def __repr__(self):
        return f'Rover: {self.x_position} {self.y_position} {self.direction}'

    def __str__(self):
        return f'{self.x_position} {self.y_position} {self.direction}'
