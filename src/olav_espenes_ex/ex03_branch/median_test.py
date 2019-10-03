# -*- coding: utf-8 -*-

__author__ = 'Olav Vikoren Espenes'
__email__ = 'olaves@nmbu.no'


def median(data):
    """
    Returns median of imput data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

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
    assert median(data) = 3