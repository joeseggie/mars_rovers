'''
Test Rover
'''
import pytest

from grid import Grid
from rover import Rover
from rover_command_handlers import (
    north_left_turn, north_right_turn, east_right_turn, east_left_turn,
    south_left_turn, south_right_turn, west_left_turn, west_right_turn,
    move_east, move_north, move_south, move_west)


def test_ok_rover_setup():
    rover = Rover('1 2 N', Grid(4, 5))
    assert str(rover) == '1 2 N'
    assert repr(rover) == 'Rover: <1 2 N>'


def test_invalid_rover_setup():
    with pytest.raises(ValueError):
        _ = Rover('1 2 NE', Grid(4, 5))


def test_turn_left():
    rover = Rover('1 2 N', Grid(4, 5))
    rover.process_command(north_left_turn)
    assert str(rover) == '1 2 W'
    assert repr(rover) == 'Rover: <1 2 W>'


def test_turn_right():
    rover = Rover('1 2 N', Grid(4, 5))
    rover.process_command(north_right_turn)
    assert str(rover) == '1 2 E'
    assert repr(rover) == f'Rover: <1 2 E>'


@pytest.mark.parametrize("current_position, new_position", [
    ('1 2 N', '1 3 N'),
    ('1 2 S', '1 1 S'),
    ('3 3 E', '4 3 E'),
    ('3 3 W', '2 3 W'),
])
def test_move(current_position, new_position):
    rover = Rover(current_position, Grid(5, 5))
    if rover.direction == 'N':
        rover = rover.process_command(move_north)
    elif rover.direction == 'E':
        rover = rover.process_command(move_east)
    elif rover.direction == 'S':
        rover = rover.process_command(move_south)
    elif rover.direction == 'W':
        rover = rover.process_command(move_west)

    assert str(rover) == new_position
    assert repr(rover) == f'Rover: <{new_position}>'


@pytest.mark.parametrize("current_position, instructions, new_position", [
    ('1 2 N', 'LMLMLMLMM', '1 3 N'),
    ('3 3 E', 'MMRMMRMRRM', '5 1 E'),
])
def test_interview(current_position, instructions, new_position):
    rover = Rover(current_position, Grid(5, 5))
    for instruction in list(instructions):
        print(rover)
        if instruction == 'L' and rover.direction == 'N':
            rover = rover.process_command(north_left_turn)
        elif instruction == 'R' and rover.direction == 'N':
            rover = rover.process_command(north_right_turn)
        elif instruction == 'L' and rover.direction == 'E':
            rover = rover.process_command(east_left_turn)
        elif instruction == 'R' and rover.direction == 'E':
            rover = rover.process_command(east_right_turn)
        elif instruction == 'L' and rover.direction == 'S':
            rover = rover.process_command(south_left_turn)
        elif instruction == 'R' and rover.direction == 'S':
            rover = rover.process_command(south_right_turn)
        elif instruction == 'L' and rover.direction == 'W':
            rover = rover.process_command(west_left_turn)
        elif instruction == 'R' and rover.direction == 'W':
            rover = rover.process_command(west_right_turn)
        elif instruction == 'M' and rover.direction == 'N':
            rover = rover.process_command(move_north)
        elif instruction == 'M' and rover.direction == 'E':
            rover = rover.process_command(move_east)
        elif instruction == 'M' and rover.direction == 'S':
            rover = rover.process_command(move_south)
        elif instruction == 'M' and rover.direction == 'W':
            rover = rover.process_command(move_west)

    assert str(rover) == new_position
    assert repr(rover) == f'Rover: <{new_position}>'
