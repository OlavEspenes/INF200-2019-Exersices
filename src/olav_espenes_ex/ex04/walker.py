# -*- coding: utf-8 -*-

__author__ = 'Olav Espenes'
__email__ = 'olaves@nmbu.no'

import random

class Walker:
    def __init__(self, start, home):
        self.position = start
        self.home = home
        self.steps = 0

    def move(self):
        self.steps += 1
        throw = random.uniform(0, 2)
        self.position += 1 if throw >= 1 else -1

    def is_at_home(self):
        return True if self.position == self. home else False


