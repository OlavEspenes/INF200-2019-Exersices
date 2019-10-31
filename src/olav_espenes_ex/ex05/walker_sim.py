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

class Simulation:
    def __init__(self, start, home, seed):
        self.start = start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        a_walker = Walker(self.start, self.home)
        while not a_walker.is_at_home():
            a_walker.move()
        return a_walker.get_steps()

    def run_simulation(self, num_walks):
        return[self.single_walk() for _ in range(num_walks)]

if __name__=='__main__':
    seed = [12345, 12345, 54321]
    for one_seed in range(1,3):
        print(Simulation(0,10,seed(one_seed)).run_simualtion(20))
    for one_seed in range(1,3):
        print(Simulation(10,0,seed(one_seed)).run_simulation(20))
