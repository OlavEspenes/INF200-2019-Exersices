# -*- coding: utf-8 -*-

__author__ = 'Olav Espenes'
__email__ = 'olaves@nmbu.no'

from walker_sim import Walker
from walker_sim import Simulation


class BoundedWalker(Walker):

    def __init__(self, start, home, left_limit, right_limit):
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit

        if not (left_limit <= start <= right_limit):
            raise ValueError('The start position is not inside the input'
                             ' limit interval')
        if not (left_limit <= home <= right_limit):
            raise ValueError('The home position is not inside the input'
                             ' interval limit')

    def move(self):

        super().move()
        if self.position < self.left_limit:
            self.position = self.left_limit
        elif self.position > self.right_limit:
            self.position = self.right_limit

class BoundedSimulation(Simulation):

    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):

        one_walker = BoundedWalker(self.start, self.home, self.left_limit,
                                   self.right_limit)
        steps = 0
        while not one_walker.is_at_home():
            one_walker.move()
            steps += 1
        return steps

if __name__ == '__main__':
    for l_limit in [0, -10, -100, -1000, -10000]:
        a_walk = BoundedSimulation(0, 20, 12345, l_limit, 20).run_simulation(20)
        print('Left boundary: {}: {}'.format(l_limit, a_walk))
