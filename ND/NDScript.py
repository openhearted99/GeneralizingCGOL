# 2018 Theodore Pena and Andrew Feder
# Licensed under the MIT License

# Stuff we need:
from __future__ import division, print_function
import sys
import numpy as np
import time


# Classes:
class Space(object):
    def __init__(self, *dimensions):
        if all(isinstance(i, int) for i in dimensions):
            self.space = np.array(dimensions)
        else:
            sys.exit("Error!")


if __name__ == '__main__':
    grid = Space(3, 3, 3)
