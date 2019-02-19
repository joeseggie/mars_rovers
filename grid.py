'''
Plateau grid.
'''


class Grid:

    def __init__(
        self,
        x_right_top_coordinate: int,
        y_right_top_coordinate: int
    ):
        '''
        Constructor.

        Parameters
        ----------
        x_top_coordinate {int}
            X coordinate for the top right corner of the grid.
        y_top_coordinate {int}
            Y coordinate for the top right corner of the grid.
        '''
        if x_right_top_coordinate <= 0 or y_right_top_coordinate <= 0:
            raise ValueError('Invalid coordinates set for the grid.')

        self.x_left_bottom_coordinate = 0
        self.y_left_bottom_coordinate = 0
        self.x_right_top_coordinate = x_right_top_coordinate
        self.y_right_top_coordinate = y_right_top_coordinate

    def __repr__(self):
        return f'Grid: {self.x_right_top_coordinate} x'\
            f' {self.y_right_top_coordinate}'
