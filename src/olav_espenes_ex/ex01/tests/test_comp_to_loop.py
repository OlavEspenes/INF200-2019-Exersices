from ..comp_to_loop import squares_by_loop
from math import sqrt

# importerer funksjon fra annen fil.


def test_zero_input_yields_lenght_zero():
    assert len(squares_by_loop(0)) == 0


def test_one_input_yields_length_one():
    assert len(squares_by_loop(1)) == 1


def test_correct_number_of_outputs():
    assert len(squares_by_loop(0)) == 0
    assert len(squares_by_loop(1)) == 1
    assert len(squares_by_loop(2)) == 1


def is_square(x):
    return abs(sqrt(x) - int(sqrt(x))) < 1e-10


def test_squares_by_loop_produces_squares():
    for number in squares_by_loop(50):



