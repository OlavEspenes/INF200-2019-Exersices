# -*- coding: utf-8 -*-

__author__ = 'Olav Vikoren Espenes'
__email__ = 'olaves@nmbu.no'

import pytest


def median(data):
    """
    Returns median of imput data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    if data == []:
        raise ValueError
    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))

def test_one_element_median():
    """Test that median works on one element list.
    """
    assert median([3]) == 3

def test_odd_numbers_median():
    """Test that median works on lists with odd numbers.
    """
    data = [3, 9, 7, 11, 1]
    assert median(data) == 7

def test_even_numbers_median():
    """Test that median works on lists with even numbers.
    """
    data = [8, 6, 2, 4, 12]
    assert median(data) == 6


def test_ordered_list_median():
    """Test that median works on ordered lists.
    """
    data = [1, 2, 3, 4, 5]
    assert median(data) == 3

def test_revers_ordered_median():
    """Test that median works on revers-ordered lists
    """
    data = [5, 4, 3, 2, 1]
    assert median(data) == 3

def test_unordered_elements_median():
    """Test that median works on lists with unordered elements
    """
    data = [5, 7, 2, 13, 9, 1]
    assert median(data) == 6

def test_value_error():
    with pytest.raises(ValueError):
        median([])

def test_original_data_unchanged():
    original_data = [2, 4, 6, 8, 10]
    median(original_data)
    assert original_data == [2, 4, 6, 8, 10]





