'''
Handler of the commands that are issued to the rover.
'''
from rover import Rover


def north_left_turn(rover: Rover) -> Rover:
    '''
    Command to turn a North facing rover left.

    Parameters
    ----------
    rover : Rover
        Rover receiving the command.

    Returns
    -------
    Rover
        State of the rover after processing the command.
    '''
    rover.direction = 'W'
    return rover


def north_right_turn(rover: Rover) -> Rover:
    '''
    Command to turn a North facing rover right.

    Parameters
    -----------
    rover : Rover
        Rover receiving the command.

    Returns
    -------
    Rover
        State of the rover after processing the command.
    '''
    rover.direction = 'E'
    return rover


def east_left_turn(rover: Rover) -> Rover:
    '''
    Command to turn an East facing rover left.

    Parameters
    ----------
    rover : Rover
        Rover receiving the command.

    Returns
    -------
    Rover
        State of the rover after processing the command.
    '''
    rover.direction = 'N'
    return rover


def east_right_turn(rover: Rover) -> Rover:
    '''
    Command to turn an East facing rover right.

    Parameters
    ----------
    rover : Rover
        Rover receiving the command.

    Returns
    -------
    Rover
        State of the rover after processing the command.
    '''
    rover.direction = 'S'
    return rover


def south_left_turn(rover: Rover) -> Rover:
    '''
    Command to turn a South facing rover left.

    Parameters
    ----------
    rover : Rover
        Rover receiving the command.

    Results
    -------
    Rover
        State of the rover after processing the command.
    '''
    rover.direction = 'E'
    return rover


def south_right_turn(rover: Rover) -> Rover:
    '''
    Command to turn a South facing rover right.

    Parameters
    ----------
    rover : Rover
        Rover receiving the command.

    Returns
    -------
    Rover
        State of the rover after processing the command.
    '''
    rover.direction = 'W'
    return rover


def west_left_turn(rover: Rover) -> Rover:
    '''
    Command to turn a West facing rover left.

    Parameters
    ----------
    rover : Rover
        Rover receiving the command.

    Returns
    -------
    Rover
        State of the rover after processing the command.
    '''
    rover.direction = 'S'
    return rover


def west_right_turn(rover: Rover) -> Rover:
    '''
    Command to turn a West facing rover right.

    Parameters
    ----------
    rover : Rover
        Rover receiving the command.

    Returns
    -------
    Rover
        State of the rover after processing the command.
    '''
    rover.direction = 'N'
    return rover


def move_north(rover: Rover) -> Rover:
    '''
    Command to move a rover in the northern direction.

    Parameters
    ----------
    rover : Rover
        Rover receiving the command.

    Returns
    -------
    Rover
        State of the rover after processing the command.
    '''
    if rover.y_position >= rover.grid.y_right_top_coordinate:
        raise ValueError('Invalid move: rover can not go overboard')
    rover.y_position += 1
    return rover


def move_east(rover: Rover) -> Rover:
    '''
    Command to move a rover in the eastern direction.

    Parameters
    ----------
    rover : Rover
        Rover receiving the command.

    Returns
    -------
    Rover
        State of the rover after processing the command.
    '''
    if rover.x_position >= rover.grid.x_right_top_coordinate:
        raise ValueError('Invalid move: rover can not go overboard')
    rover.x_position += 1
    return rover


def move_south(rover: Rover) -> Rover:
    '''
    Command to move a rover in the southern direction.

    Parameters
    ----------
    rover : Rover
        Rover receiving the command.

    Returns
    -------
    Rover
        State of the rover after processing the command.
    '''
    if rover.y_position <= rover.grid.y_left_bottom_coordinate:
        raise ValueError('Invalid move: rover can not go overboard')
    rover.y_position -= 1
    return rover


def move_west(rover: Rover) -> Rover:
    '''
    Command to move a rover in the western direction.

    Parameters
    ----------
    rover : Rover
        Rover receiving the command.

    Returns
    -------
    Rover
        State of the rover after processing the command.
    '''
    if rover.x_position <= rover.grid.x_left_bottom_coordinate:
        raise ValueError('Invalid move: rover can not go overboard')
    rover.x_position -= 1
    return rover
