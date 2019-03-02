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

    def process_command(self, command_handler):
        self = command_handler(self)
        return self

    def __repr__(self):
        return f'Rover: <{self.x_position} {self.y_position} {self.direction}>'

    def __str__(self):
        return f'{self.x_position} {self.y_position} {self.direction}'
