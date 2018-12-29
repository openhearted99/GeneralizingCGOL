# 2018 Theodore Pena and Andrew Feder
# Licensed under the MIT License

# Stuff we need:
from __future__ import division, print_function
import sys
import numpy as np
import time
from random import randint


# Constants
len_hypercube = 100
birth_num = 3
overcrowding_num = 4
starvation_num = 2


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
            for i in np.arange(dimensions[0]):
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
        for i in np.arange(num_entries2seed):
            while True:
                random_cell_coordinates = []
                for j in np.arange(self.space.ndim):
                    random_cell_coordinates.append(randint(0,
                                                           self.space.shape[j]
                                                           - 1))
                    if self.space[tuple(random_cell_coordinates)] == 1:
                        continue
                    elif self.space[tuple(random_cell_coordinates)] == 0:
                        self.space[tuple(random_cell_coordinates)] = 1
                        break

    def find_neighbors(self, *cell_coordinates):
        num_dim = self.space.ndim

    def tick(self, iterations):
        num_dim = self.space.num_dim
        space_shape = self.space.shape
        for iteration in np.arange(iterations):
            _temp_space = np.zeros(space_shape, dtype=int)
            for dimension in np.arange(num_dim):
                for 

if __name__ == '__main__':
    k = Space(3)
    k.seed_grid()
    k.print_space()
