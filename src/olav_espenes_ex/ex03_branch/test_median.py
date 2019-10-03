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




