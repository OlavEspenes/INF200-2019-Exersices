# -*- coding: utf-8 -*-

__author__ = 'Olav Espenes'
__email__ = 'olaves@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.a = 16807
        self.m = 2 ** 31 - 1


    def rand(self):
        while True:
            self.seed = self.a * self.seed % self.m
            return self.seed


class ListRand:
    def __init__(self, list):
        self.list = list
        self.idx = 0

    def rand(self):
        self.idx += 1
        if self.idx > len(self.list):
            raise RuntimeError('Cannot make a list longer then input')
        else:
            return self.list[self.idx-1]


if __name__=='__main__':
    LCG = LCGRand(20)
    LR = ListRand([1, 2, 3])
    for _ in range(3):
        print(LCG.rand())
        print(LR.rand())
