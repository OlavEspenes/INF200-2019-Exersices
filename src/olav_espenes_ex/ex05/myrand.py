# -*- coding: utf-8 -*-

__author__ = 'Olav Espenes'
__email__ = 'olaves@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 7**5
        self.m = 2 ** 31 - 1

    def rand(self):
        while True:
            self.seed = (self.a * self.seed) % self.m
            return self.seed

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        return RandIter(self, -1)


class RandIter:
    def __init__(self, random_number_generator, length):
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        print('Initialising iterator')
        if self.num_generated_numbers is not None:
            raise RuntimeError(
                'Can only be initialised as an iterator once'
            )
        self.num_generated_numbers = -1
        return self

    def __next__(self):
        self.num_generated_numbers += 1
        if self.num_generated_numbers is None:
            raise RuntimeError(
                'Cannot call `next`before iter is initialised'
            )
        if self.num_generated_numbers == self.length:
            raise StopIteration
        return self.generator.rand()
