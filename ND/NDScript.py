# 2018 Theodore Pena and Andrew Feder
# Licensed under the MIT License

# Stuff we need:
from __future__ import division, print_function
import sys
import numpy as np
import time
from random import randint


# Constants
len_hypercube = 1


# Classes:
# This class handles the space in which the game is played.
class Space(object):
    # If the initialization is passed a single number, it interpretes that as
    # the number of dimensions of a n-dimensional hypercube, where each side is
    # of length len_hypercube. Otherwise, the dimensions can be input manually.
    def __init__(self, *dimensions):
        if len(dimensions) > 1:
            if all(isinstance(i, int) for i in dimensions):
                self.space = np.zeros(dimensions, dtype=int)
            else:
                sys.exit("Error! The dimensions of the space must be integers")
        elif len(dimensions) == 1:
            _size_cube = []
            for i in range(dimensions[0]):
                _size_cube.append(len_hypercube)
            size_cube = tuple(_size_cube)
            self.space = np.zeros(size_cube, dtype=int)
        else:
            sys.exit("Error! The gamespace must have at least one dimension.")

    # Basic print function.
    def print_space(self):
        print(self.space)

    # Seeds the gamespace by randomlly filling in 1% of the total cells.
    def seed_grid(self):
        num_entries2seed = randint(0, round(self.space.size*.01))
        for i in range(num_entries2seed):
            while True:
                random_cell_coordinates = []
                for j in range(self.space.ndim):
                    random_cell_coordinates.append(randint(0,
                                                           self.space.shape[j]
                                                           - 1))
                    if self.space[tuple(random_cell_coordinates)] == 1:
                        continue
                    elif self.space[tuple(random_cell_coordinates)] == 0:
                        self.space[tuple(random_cell_coordinates)] = 1
                        break


if __name__ == '__main__':
    k = Space(3)
    k.seed_grid()
    k.print_space()
