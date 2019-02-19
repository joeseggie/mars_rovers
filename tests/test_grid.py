'''
Unit tests for Grid
'''
import pytest

from grid import Grid


def test_ok_grid_setup():
    test_grid = Grid(5, 5)
    assert isinstance(test_grid, Grid)
    expected = "Grid: 5 x 5"
    assert repr(test_grid) == expected


def test_invalid_grid_setup():
    with pytest.raises(ValueError):
        _ = Grid(0, 0)
