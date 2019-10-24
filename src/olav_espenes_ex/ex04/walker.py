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


    def get_position(self):
        return self.position


    def get_steps(self):
        return self.steps


    def walk_me_home_return_steps(self):
        while not self.is_at_home():
            self.move()
        return self.steps



if __name__=='__main__':
    print(f'Distance:   1 -> Path lengths: '
        f'{[Walker(0, 1).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance:   2 -> Path lengths: '
        f'{[Walker(0, 2).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance:   5 -> Path lengths: '
        f'{[Walker(0, 5).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance:  10 -> Path lengths: '
        f'{[Walker(0, 10).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance:  20 -> Path lengths: '
        f'{[Walker(0, 20).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance:  50 -> Path lengths: '
        f'{[Walker(0, 50).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance: 100 -> Path lengths: '
        f'{[Walker(0, 100).walk_me_home_return_steps() for _ in range(5)]}')

