# -*- coding: utf-8 -*-
from hypothesis import given, strategies


__author__ = 'Olav Vikoren Espenes'
__email__ = 'olaves@nmbu.no'


def bubble_sort(file):
    """Sort list with number in increasing order
    """
    data_list = list(file)
    length_list = len(file)

    for element in range(length_list):
        for sec_element in range(length_list - element - 1):
            if data_list[sec_element] > data_list[sec_element + 1]:
                data_list[sec_element], data_list[sec_element + 1] = \
                    data_list[sec_element + 1], data_list[sec_element]
    return data_list


def test_empty():
    """Test that the sorting function works for empty list.
    """

    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list.
    """
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """Test that the sorting function returns a new object.
    """
    data = [3, 2, 1]
    assert bubble_sort(data) != data


def test_original_unchanged():
    """Test that sorting leaves the original data unchanged.
    """

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data != sorted_data


def test_sort_sorted():
    """Test that sorting works on sorted data.
    """
    data = [1, 2, 3]
    assert bubble_sort(data)


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data.
    """

    data = [3, 2, 1]
    assert bubble_sort(data) == [1, 2, 3]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements.
    """

    data = [1, 1, 1]
    assert bubble_sort(data)


@given(strategies.lists(strategies.integers()))
def test_sorting(lists):
    """Test sorting for various test cases.
    """
    sorted_list = bubble_sort(lists)
    for small, large in zip(sorted_list[:-1], sorted_list[1:]):
        assert small <= large
