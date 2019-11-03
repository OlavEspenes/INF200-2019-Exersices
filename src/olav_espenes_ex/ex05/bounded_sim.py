# -*- coding: utf-8 -*-

__author__ = 'Olav Espenes'
__email__ = 'olaves@nmbu.no'


class BoundedWalker(Walker):

    def __init__(self, start, home, left_limit, right_limit)
        if not (left_limit <= start <= right_limit)
            raise ValueError('The start position is not inside the input'
                             ' limit interval')
        if not (left_limit <= home <= right_limit)
            raise ValueError('The home position is not inside the input'
                             ' interval limit')
        super_class().__init__(start, home)
        self.left = left_limit
        self.right = right_limit

    def move(self):

        super_class().move()
        if self.position < self.left:
            self. position = self.left
        elif self. position > self.right:
            self.position = self.right


class BoundedSimulation(Simulation):

    def __init__(self, start, home, seed, left_limit, right_limit):
        super_class().__init__(start, home, seed)
        self.left = left_limit
        self.right = right_limit

    def single_walk(self):

        one_walker = BoundedWalker(self.start, self.home, self.left,
                                   self.right)
        steps = 0
        while not walker.is_at_home():
            walker.move()
            steps += 1
        return steps

    