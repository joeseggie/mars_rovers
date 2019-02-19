'''
Test Rover
'''
import pytest

from grid import Grid
from rover import Rover


def test_ok_rover_setup():
    rover = Rover('1 2 N', Grid(4, 5))
    assert str(rover) == '1 2 N'
    assert repr(rover) == 'Rover: 1 2 N'


def test_invalid_rover_setup():
    with pytest.raises(ValueError):
        _ = Rover('1 2 NE', Grid(4, 5))


def test_turn_left():
    rover = Rover('1 2 N', Grid(4, 5))
    rover.turn_left()
    assert str(rover) == '1 2 W'
    assert repr(rover) == 'Rover: 1 2 W'


def test_turn_right():
    rover = Rover('1 2 N', Grid(4, 5))
    rover.turn_right()
    assert str(rover) == '1 2 E'
    assert repr(rover) == 'Rover: 1 2 E'


@pytest.mark.parametrize("current_position, new_position", [
    ('1 2 N', '1 3 N'),
    ('1 2 S', '1 1 S'),
    ('3 3 E', '4 3 E'),
    ('3 3 W', '2 3 W'),
])
def test_move(current_position, new_position):
    rover = Rover(current_position, Grid(5, 5))
    rover.move()
    assert str(rover) == new_position
    assert repr(rover) == f'Rover: {new_position}'


@pytest.mark.parametrize("current_position, instructions, new_position", [
    ('1 2 N', 'LMLMLMLMM', '1 3 N'),
    ('3 3 E', 'MMRMMRMRRM', '5 1 E'),
])
def test_interview(current_position, instructions, new_position):
    rover = Rover(current_position, Grid(5, 5))
    for instruction in list(instructions):
        if instruction == 'L':
            rover.turn_left()
        if instruction == 'R':
            rover.turn_right()
        if instruction == 'M':
            rover.move()

    assert str(rover) == new_position
    assert repr(rover) == f'Rover: {new_position}'
